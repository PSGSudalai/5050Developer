from apps.BASE.serializers import ReadOnlySerializer, WriteOnlySerializer
from apps.ADMIN.models import Event

class EventWebReadSerializer(ReadOnlySerializer):
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
