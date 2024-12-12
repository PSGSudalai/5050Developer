from apps.ACCESS.models import User
from apps.ADMIN.models import Subscription,Event,Payment
from apps.BASE.serializers import ReadOnlySerializer, read_serializer


class SubcriptionReadSerializer(ReadOnlySerializer):
    user_detail = read_serializer(User,meta_fields=["id","uuid","name"])(source="user")
    event_detail = read_serializer(Event,meta_fields=["id","uuid","title","status","image","about","point","start_time","end_time","date"])(source="event")
    payment_detail = read_serializer(Payment,meta_fields=["id","uuid","status"])(source="payment")
    class Meta(ReadOnlySerializer.Meta):
        model = Subscription
        fields = [
            "id",
            "uuid",
            "user_detail",
            "event_detail",
            "payment_detail",
            "amount"
        ]
        