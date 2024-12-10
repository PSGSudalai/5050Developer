
from apps.BASE.serializers import ReadOnlySerializer, WriteOnlySerializer, read_serializer
from apps.ADMIN.models import Event,EventImage,DemoVideo

class EventWebReadSerializer(ReadOnlySerializer):
    image_detail = read_serializer(EventImage,meta_fields=["id","uuid","file"])(source="image")
    video_detail = read_serializer(DemoVideo,meta_fields=["id","uuid","file"])(source="video")
    class Meta(ReadOnlySerializer.Meta):
        model =Event
        fields = [
            "id",
            "uuid",
            "title",
            "status",
            "description",
            "point",
            "date",
            "start_time",
            "end_time",
            "image_detail",
            "video_detail",
            "about",
            "keyskill"
        ]
