from apps.ADMIN.serializers import EventReadSerializer,EventWriteSerializer
from apps.BASE.views import ListAPIViewSet, CUDAPIViewSet
from apps.ADMIN.models import Event

class EventListAPIViewSet(ListAPIViewSet):
    queryset = Event.objects.all()
    serializer_class = EventReadSerializer

class EventCUDAPIViewSet(CUDAPIViewSet):
    queryset = Event.objects.all()
    serializer_class = EventWriteSerializer