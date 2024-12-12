from apps.ADMIN.models import Subscription
from apps.BASE.base import AppAPIView
from apps.BASE.views import ListAPIViewSet
from apps.WEBSITE.serializers import SubcriptionReadSerializer


class SubscriptionListAPIView(ListAPIViewSet):
    serializer_class = SubcriptionReadSerializer
    def get_queryset(self):
        user = self.get_authenticated_user()
        return Subscription.objects.filter(user=user)
    


class SubscriptionTableMeta(AppAPIView):
    all_table_columns={
        "event_detail.title":"Title",
        "event_detail.date":"Date",
        "payment_detail.status":"Status",
        "amount":"Amount"
    }

    all_filters={}

    def get(self,*args,**kwargs):
        data ={
            "Column":self.all_table_columns
        }
        return self.send_response(data)
    