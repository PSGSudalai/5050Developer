from apps.ADMIN.serializers import CompletedReadSerializer
from apps.BASE.views import ListAPIViewSet
from apps.ADMIN.models import Event


class CompleteEventListAPIView(ListAPIViewSet):
    filterset_fields ={
        "title":["exact"],
        
    }
    queryset = Event.objects.filter(status='Completed').order_by("-created")
    serializer_class = CompletedReadSerializer


    all_table_columns={
        "title":"Event Name",
        "status":"Status",
        "date":"Date"
    }


    def get_meta_for_table(self):
        data={
            "Column":self.all_table_columns
        }
        return data