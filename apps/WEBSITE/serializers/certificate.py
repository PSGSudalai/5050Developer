from datetime import datetime
from apps.BASE.serializers import ReadOnlySerializer, read_serializer
from apps.ADMIN.models import Event,EventImage
from rest_framework import serializers

class CertificateReadSerializer(ReadOnlySerializer):
    image_detail = read_serializer(EventImage,meta_fields=["id","uuid","file"])(source="image")
    duration = serializers.SerializerMethodField()
    class Meta(ReadOnlySerializer.Meta):
        model = Event
        fields = [
            "id",
            "uuid",
            "image_detail",
            "title",
            "date",
            "point",
            "start_time",
            "end_time",
            "duration"
        ]


    def get_duration(self, obj):
        try:
            # Parse start_time and end_time
            start_time = datetime.strptime(obj.start_time, "%H:%M")
            end_time = datetime.strptime(obj.end_time, "%H:%M")

            # Calculate the duration
            duration = end_time - start_time

            # Convert duration to hours (as a float)
            hours = duration.total_seconds() / 3600

            return f"{hours:.2f} hours" 

        except (ValueError, TypeError) as e:
            return "Invalid time format"
        