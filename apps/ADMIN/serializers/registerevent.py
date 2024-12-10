from rest_framework import serializers
from apps.ADMIN.models import RegisterEvent,Event
from apps.BASE.serializers import ReadOnlySerializer, read_serializer


class RegisterEventReadSerializer(ReadOnlySerializer):
    event_detail = read_serializer(Event, meta_fields=["id", "uuid", "title", "date"])(source="event")  # Adjusted source field
    user_count = serializers.SerializerMethodField()
    total_amount = serializers.SerializerMethodField()  # Add total amount with symbol

    class Meta(ReadOnlySerializer.Meta):
        model = RegisterEvent
        fields = [
            "id",
            "uuid",
            "user_count",
            "event_detail",
            "total_amount"  
        ]
    
    def get_user_count(self, obj):
        user_count = obj.registered_users.count()  
        return user_count

    def get_total_amount(self, obj):
        per_user_amount = obj.per_user_amount if hasattr(obj, "per_user_amount") else 100  
        user_count = self.get_user_count(obj)
        total = user_count * per_user_amount
        return f"₹{total}"  