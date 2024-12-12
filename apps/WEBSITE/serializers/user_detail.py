from apps.ACCESS.models import User
from apps.BASE.serializers import ReadOnlySerializer


class UserDetailReadSerializer(ReadOnlySerializer):
    class Meta(ReadOnlySerializer.Meta):
        model = User
        fields = [
            "id",
            "uuid",
            "name",
            "email"
        ]