from datetime import datetime
from apps.ACCESS.models import User
from apps.BASE.base import AppAPIView
from apps.ADMIN.models import Event


class AdminDashboard(AppAPIView):
    def get(self,request,*args,**kwargs):
        today = datetime.now()
        current_month = today.month
        total_event_count = Event.objects.all().count()
        upcoming_count = Event.objects.filter(status__in=['Opened','Coming Soon']).count()
        total_user_count = User.objects.all().count()
        new_user_count =User.objects.filter(created__month=current_month).count()



        data ={
            "total_event_count":total_event_count,
            "upcoming_count":upcoming_count,
            "total_user_count":total_user_count,
            "new_user_count":new_user_count
        }

        return self.send_response(data)