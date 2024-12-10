from apps.ADMIN.serializers import EventReadSerializer
from apps.BASE.views import ListAPIViewSet
from apps.ADMIN.models import Event

class EventHistoryListAPIView(ListAPIViewSet):

    filterset_fields=["status"]
    queryset = Event.objects.all().order_by("-created")
    serializer_class = EventReadSerializer

    all_table_columns={
        "title":"Name",
        "status":"Status",
        "point":"Point",
        "date":"Date"
    }


    def get_meta_for_table(self):
        data ={
            "column":self.all_table_columns
        }
        return data
    