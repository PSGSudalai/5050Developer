from apps.ACCESS.models import User
from apps.ADMIN.models import Event
from apps.BASE.model_fields import AppSingleChoiceField
from apps.BASE.models import DEFAULT_BLANK_NULLABLE_FIELD_CONFIG, MAX_CHAR_FIELD_LENGTH, BaseModel
from django.db import models

from apps.HELPERS.choices import PAYMENT_STATUS

class Payment(BaseModel):
    order_id = models.CharField(max_length=MAX_CHAR_FIELD_LENGTH)
    payment_id = models.CharField(
        max_length=MAX_CHAR_FIELD_LENGTH, **DEFAULT_BLANK_NULLABLE_FIELD_CONFIG
    )
    amount = models.FloatField()
    status = AppSingleChoiceField(
        choices_config=PAYMENT_STATUS, **DEFAULT_BLANK_NULLABLE_FIELD_CONFIG
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        **DEFAULT_BLANK_NULLABLE_FIELD_CONFIG,
    )
    event = models.ForeignKey(Event,on_delete=models.SET_NULL,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)