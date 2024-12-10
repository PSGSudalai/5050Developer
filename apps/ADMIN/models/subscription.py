from apps.ACCESS.models import User
from apps.ADMIN.models import Event
from apps.BASE.models import DEFAULT_BLANK_NULLABLE_FIELD_CONFIG, BaseModel
from django.db import models


class Subscription(BaseModel):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    event = models.ForeignKey(Event,on_delete=models.SET_NULL,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    payment = models.ForeignKey("ADMIN.Payment",on_delete=models.SET_NULL,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    amount = models.IntegerField(**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    