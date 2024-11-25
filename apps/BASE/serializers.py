from datetime import datetime
from rest_framework import serializers
from rest_framework.fields import SkipField
from rest_framework.serializers import ModelSerializer, Serializer
from apps.BASE import model_fields
from apps.BASE.config import CUSTOM_ERRORS_MESSAGES
from django.db import models


class CustomErrorMessagesMixin:
    def get_display(self, field_name):
        return field_name.replace("_", " ")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in getattr(self, "fields", {}).items():
            if field.__class__.__name__ == "ManyRelatedField":
                field.error_messages.update(CUSTOM_ERRORS_MESSAGES["ManyRelatedField"])
                field.child_relation.error_messages.update(
                    CUSTOM_ERRORS_MESSAGES["PrimaryKeyRelatedField"]
                )
            elif field.__class__.__name__ == "PrimaryKeyRelatedField":
                field.error_messages.update(
                    CUSTOM_ERRORS_MESSAGES["PrimaryKeyRelatedField"]
                )
            else:
                field.error_messages.update(
                    {
                        "blank": f"Please enter your {self.get_display(field_name)}",
                        "null": f"Please enter your {self.get_display(field_name)}",
                    }
                )


class AppSerializer(CustomErrorMessagesMixin, Serializer):
    def get_initial_data(self, key, expected_type):
        _data = self.initial_data.get(key)

        if type(_data) != expected_type:
            raise SkipField()

        return _data

    def get_user(self):
        return self.get_request().user

    def get_request(self):
        return self.context.get("request", None)


class AppModelSerializer(AppSerializer, ModelSerializer):
    class Meta:
        pass


class WriteOnlySerializer(AppModelSerializer):
    def create(self, validated_data):
        instance = super().create(validated_data=validated_data)

        if hasattr(instance, "created_by") and not instance.created_by:
            user = self.get_user()
            instance.created_by = user if user and user.is_authenticated else None
            instance.save()

        if hasattr(instance, "point_created_modified_date"):
            instance.point_created_modified_date = datetime.now()
            instance.save()

        return instance

    def get_validated_data(self, key=None):
        if not key:
            return self.validated_data
        return self.validated_data[key]

    def __init__(self, *args, **kwargs):
        for field in self.Meta.fields:
            self.Meta.extra_kwargs.setdefault(field, {})
            self.Meta.extra_kwargs[field]["required"] = True

        super().__init__(*args, **kwargs)

    class Meta(AppModelSerializer.Meta):
        model = None
        fields = []
        extra_kwargs = {}

    def to_internal_value(self, data):
        data = super().to_internal_value(data=data)
        for k, v in data.items():
            if not v and v not in [False, 0, []]:
                data[k] = None

        return data

    def to_representation(self, instance):
        return self.get_meta_initial()

    def serialize_choices(self, choices: list):
        from apps.BASE.helpers import get_display_name_for_slug

        return [{"id": _, "identity": get_display_name_for_slug(_)} for _ in choices]

    def serialize_for_meta(self, queryset, fields=None):
        if not fields:
            fields = ["id", "identity"]

        return simple_serialize_queryset(fields=fields, queryset=queryset)

    def get_meta(self) -> dict:
        return {}

    def get_meta_for_create(self):
        return {
            "meta": self.get_meta(),
            "initial": {},
        }

    def get_meta_for_update(self):
        return {
            "meta": self.get_meta(),
            "initial": self.get_meta_initial(),
            "urls": self.get_meta_urls(),  # file & images
        }

    def get_meta_urls(self) -> dict:
        from apps.BASE.models import FileOnlyModel

        instance = self.instance
        urls = []

        for field_name, field in self.fields.items():
            field = self.Meta.model.get_model_field(field_name)

            if field and field.related_model:
                related_instance = getattr(instance, field_name, None)

                if isinstance(related_instance, (models.Manager, models.QuerySet)):
                    url_list = [
                        {field_name: item.file.url, "id": item.id}
                        for item in related_instance.all()
                        if hasattr(item, "file") and item.file
                    ]
                    urls.extend(url_list)

                elif (
                    related_instance
                    and hasattr(related_instance, "file")
                    and related_instance.file
                ):
                    urls.append(
                        {
                            field_name: related_instance.file.url,
                            "id": related_instance.id,
                        }
                    )

        return urls

    def get_meta_initial(self):
        instance = self.instance
        initial = {
            field_name: getattr(instance, field_name, None)
            for field_name in ["id", "uuid", *self.fields.keys()]
        }

        for k, v in initial.items():
            if hasattr(initial[k], "pk"):
                initial[k] = v.pk

            if not instance.__class__.get_model_field(k, None):
                continue

            if instance.__class__.get_model_field(k).many_to_many:
                initial[k] = getattr(instance, k).values_list("pk", flat=True)
        return initial


class ReadOnlySerializer(AppModelSerializer):
    class Meta(AppModelSerializer.Meta):
        pass

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError


# get_app_read_only_serializer
def read_serializer(
    meta_model, meta_fields=None, init_fields_config=None, queryset=None
):
    if meta_fields is None:
        meta_fields = ["id", "uuid", "identity"]

    class _Serializer(ReadOnlySerializer):
        class Meta(ReadOnlySerializer.Meta):
            model = meta_model
            fields = meta_fields

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            if init_fields_config:
                for field, value in init_fields_config.items():
                    self.fields[field] = value

    return _Serializer


def simple_serialize_queryset(fields, queryset):
    if "id" in fields:
        return [
            {**_, "id": str(_["id"])} for _ in queryset.only(*fields).values(*fields)
        ]

    return queryset.only(*fields).values(*fields)


# def simple_serialize_instance(
#     instance, keys: list, parent_data: dict = None, display=None
# ) -> dict:

#     def _serialize_value(_v):
#         if type(_v) in [int, float]:
#             return _v

#         return str(_v) if _v else _v

#     if not parent_data:
#         parent_data = {}

#     if not display:
#         display = {}

#     for key in keys:
#         if "." in key:

#             _keys, _inter_value = key.split("."), None
#             for _k in _keys:
#                 if not _inter_value:
#                     _inter_value = getattr(instance, _k, None)
#                 else:
#                     _inter_value = getattr(_inter_value, _k, None)
#             parent_data[key] = _serialize_value(_inter_value)
#         else:
#             parent_data[key] = _serialize_value(getattr(instance, key, None))
#     for k, d in display.items():
#         parent_data[d] = parent_data.pop(k)

#     return parent_data


# class FileModelToURLField(serializers.Field):
#     def to_internal_value(self, data):
#         raise NotImplementedError

#     def to_representation(self, value):
#         return value.file.url
