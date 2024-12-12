from apps.ACCESS.models import User
from apps.ADMIN.serializers import SubscriptionReadSerializer
from apps.BASE.base import AppAPIView
from apps.BASE.views import ListAPIViewSet
from apps.ADMIN.models import Event,Subscription


class SubscriptionListAPIView(ListAPIViewSet):
    serializer_class =SubscriptionReadSerializer
    def get_queryset(self):
        uuid = self.kwargs["uuid"]
        event = Event.objects.get(uuid=uuid)
        return Subscription.objects.filter(event=event)
    

class SubscriptionAPIView(AppAPIView):
    def post(self,request,*args,**kwargs):
        uuid = request.data.get("uuid")
        status = request.data.get("status")

        try:
            subscription = User.objects.get(uuid = uuid)
            subscription.status = status
            subscription.save()
            return self.send_response({"success":"Status Update Successfully"})
        except User.DoesNotExist:
            # Handle the case where the quotation is not found
            return self.send_error_response(f"No User found with UUID: {uuid}")
        except Exception as e:
            # Catch any other exceptions
            return self.send_error_response(f"An error occurred: {str(e)}")
        
class SubscriptionTableMeta(AppAPIView):
    all_table_column ={
        "event_detail.title":"Title",
        "user_detail.status":"Status",
        "amount":"Amount"
    }

    def get(self,*args,**kwargs):
        data = {
            "Column":self.all_table_column
        }
        return self.send_response(data)

        