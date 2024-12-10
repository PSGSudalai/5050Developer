from apps.ADMIN.models import Event
from apps.BASE.models import DEFAULT_BLANK_NULLABLE_FIELD_CONFIG, BaseModel
from django.db import models

class RegisterEvent(BaseModel):
    event = models.ForeignKey(Event,on_delete=models.SET_NULL,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    amount = models.IntegerField(**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    point =models.IntegerField(**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
