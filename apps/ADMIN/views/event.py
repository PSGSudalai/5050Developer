from apps.ADMIN.serializers import EventReadSerializer,EventWriteSerializer
from apps.BASE.views import ListAPIViewSet, CUDAPIViewSet
from apps.ADMIN.models import Event
from datetime import date

class EventListAPIViewSet(ListAPIViewSet):
    queryset = Event.objects.exclude(status__in=['Closed', 'Completed']).order_by("-created")
    serializer_class = EventReadSerializer

    all_filters ={}

    all_table_columns ={
        "title":"Name",
        "status":"Status",
        "point":"Point",
        "date":"Date",
        "start_time":"Start Time",
        "end_time":"End Time",

    }

    def get_meta_for_table(self):
        data={
            "column":self.get_table_columns()
        }
        return data

class EventCUDAPIViewSet(CUDAPIViewSet):
    queryset = Event.objects.all()
    serializer_class = EventWriteSerializer