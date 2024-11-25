from apps.BASE.serializers import ReadOnlySerializer, WriteOnlySerializer
from apps.ADMIN.models import Event





class EventReadSerializer(ReadOnlySerializer):
    class Meta(ReadOnlySerializer.Meta):
        model =Event
        fields = [
            "id",
            "uuid",
            "title",
            "status",
            "description",
            "point",
            "date"
        ]

class EventWriteSerializer(WriteOnlySerializer):
    class Meta(WriteOnlySerializer.Meta):
        model = Event
        fields = [
            "title",
            "status",
            "description",
            "point",
            "date"
        ]