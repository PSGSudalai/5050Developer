from apps.ADMIN.models import DemoVideo, EventImage
from apps.BASE.serializers import ReadOnlySerializer, WriteOnlySerializer, read_serializer
from apps.ADMIN.models import Event
from rest_framework import serializers


class EventReadSerializer(ReadOnlySerializer):

    image_detail = read_serializer(EventImage,meta_fields=["id","uuid","file"])(source ="image")
    video_detail = read_serializer(DemoVideo,meta_fields=["id","uuid","file"])(source="video")

    class Meta(ReadOnlySerializer.Meta):
        model = Event
        fields = [
            "id",
            "uuid",
            "image_detail",
            "title",
            "status",
            "about",
            "video_detail",
            "description",
            "point",
            "amount",  
            "date",
            "start_time",
            "end_time", 
            "keyskill"
        ]


class EventWriteSerializer(WriteOnlySerializer):
    class Meta(WriteOnlySerializer.Meta):
        model = Event
        fields = [
            "title",
            "status",
            "description",
            "point",
            "amount",
            "date",
            "start_time",
            "end_time",
            "image",
            "video",
            "keyskill",
            "about"
        ]