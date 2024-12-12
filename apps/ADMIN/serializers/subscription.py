from apps.ACCESS.models import User
from apps.ADMIN.models import Subscription,Event
from apps.BASE.serializers import ReadOnlySerializer, read_serializer


class SubscriptionReadSerializer(ReadOnlySerializer):
    user_detail = read_serializer(User,meta_fields=["id","uuid","status"])(source="user")
    event_detail = read_serializer(Event,meta_fields=["id","uuid","title"])(source="event")
    class Meta(ReadOnlySerializer.Meta):
        model = Subscription
        fields =[
            "id",
            "uuid",
            "user_detail",
            "event_detail",
            "amount",
            "created"
        ]
    