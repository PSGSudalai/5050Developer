
from apps.ADMIN.models.subscription import Subscription
from apps.BASE.base import AppAPIView
from rest_framework.permissions import IsAuthenticated
from apps.ADMIN.models import Event,Payment
from apps.BASE.payment_helper import create_razorpay_payment_order, verify_razorpay_payment_completion
from apps.WEBSITE.serializers import PaymentSerializer
from django.db import transaction


class CreateOrderView(AppAPIView):
    permission_classes =[IsAuthenticated]

    def post(self,request):
        uuid = request.data.get("uuid")
        if not uuid:
            return self.send_error_response({"error":"Invalid event"})
        
        try:
            item =Event.objects.get(uuid=uuid)
            amount = int(item.amount * 100)
        except Event.DoesNotExist:
            return self.send_error_response({"error":"event not found"})
        
        currency = "INR"

        try:
            order_response = create_razorpay_payment_order(amount,currency)

            payment = Payment.objects.create(
                order_id = order_response["id"],
                amount = amount /100,
                status = "Payment Initiated",
                event =item
            )
            serializer =PaymentSerializer(payment)
            return self.send_response(serializer.data)
        except Exception as e:
            return self.send_error_response({"error":str(e)})
        


class VerifyPaymentView(AppAPIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        razorpay_order_id = request.data.get("order_id")
        razorpay_payment_id = request.data.get("payment_id")
        razorpay_signature = request.data.get("signature")
        uuid = request.data.get("uuid")
        user = self.get_authenticated_user()

        if not all([razorpay_order_id,razorpay_payment_id,razorpay_signature]):
            return self.send_error_response({"error":"Missing Razorpay details"})
        
        if not uuid:
            return self.send_error_response({"error":"Event UUId is required"})
        
        try:
            verify_razorpay_payment_completion(
                razorpay_order_id = razorpay_order_id,
                razorpay_payment_id =razorpay_payment_id,
                razorpay_signature = razorpay_signature,
            )
            payment = Payment.objects.get(order_id = razorpay_order_id)
            payment.payment_id = razorpay_payment_id
            payment.user = user
            payment.status = "Paid",
            payment.save()

            item = Event.objects.get(uuid =uuid)

            if not item:
                return self.send_error_response({"error":"Item not found"})
            
            amount = item.amount
            with transaction.atomic():
                sub = Subscription.objects.create(
                    user= user,
                    event = item,
                    amount = amount,
                    payment = payment,
                )

            return self.send_response({"success":"Payment successfully"})
        except Payment.DoesNotExist:
            return self.send_error_response({"error":"Payment not found"})
        except Exception as e:
            payment = Payment.objects.get(order_id = razorpay_order_id)
            payment.status ="Pending"
            payment.save()

            if "sub" in locals():
                sub.delete()
            return self.send_error_response({"error":str(e)})



            