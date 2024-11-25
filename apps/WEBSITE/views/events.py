from apps.WEBSITE.serializers import EventWebReadSerializer
from apps.BASE.views import CUDAPIViewSet, ListAPIViewSet
from apps.ADMIN.models import Event
class EventWebListViewSet(ListAPIViewSet):
    queryset=Event.objects.all()
    serializer_class=EventWebReadSerializer