from apps.BASE.serializers import ReadOnlySerializer
from apps.ADMIN.models import Event
from rest_framework import serializers



class CompletedReadSerializer(ReadOnlySerializer):
    # total_amount = serializers.SerializerMethodField()
    # user_count = serializers.SerializerMethodField()
    class Meta(ReadOnlySerializer.Meta):
        model = Event
        fields = [
            "id",
            "uuid",
            "title",
            "status",
            "description",
            "point",
            "start_time",
            "end_time",
            "amount",
            "date"
            # "total_amount",
            # "user_count"
        ]

    # def get_user_count(self ,obj):

