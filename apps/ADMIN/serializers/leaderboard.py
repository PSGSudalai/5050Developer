from apps.BASE.serializers import ReadOnlySerializer
from apps.ACCESS.models import User

class LeaderBoardReadSerializer(ReadOnlySerializer):
    class Meta(ReadOnlySerializer.Meta):
        model = User
        fields = [
            "id",
            "uuid",
            "student_id",
            "name",
            "email",
            "phone",
            "college_name"
        ]
        
