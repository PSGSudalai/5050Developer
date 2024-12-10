from apps.ADMIN.serializers import LeaderBoardReadSerializer
from apps.BASE.views import ListAPIViewSet
from apps.ACCESS.models import User

class LeaderBoardListAPIView(ListAPIViewSet):
    queryset = User.objects.all().order_by("-student_id")
    serializer_class = LeaderBoardReadSerializer

    all_table_columns={
        "student_id":"ID",
        "name":"Name",
        "email":"Email",
        "phone":"Phone",
        "college_name":"College Name"
    }
    def get_meta_for_table(self):
        data = {
            "Column":self.all_table_columns
        }
        return data

