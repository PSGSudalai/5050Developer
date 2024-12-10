from apps.ADMIN.models import Payment
from apps.BASE.serializers import WriteOnlySerializer


class PaymentSerializer(WriteOnlySerializer):
    class Meta(WriteOnlySerializer.Meta):
        model = Payment
        fields = [
            "order_id",
            "amount",
            "status",
        ]
    