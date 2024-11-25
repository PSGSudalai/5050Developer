from apps.BASE.model_fields import AppSingleChoiceField, AppSingleFileField
from apps.BASE.models import DEFAULT_BLANK_NULLABLE_FIELD_CONFIG, MAX_CHAR_FIELD_LENGTH, BaseModel
from django.db import models

from apps.HELPERS.choices import STATUS

class EventImage(BaseModel):
    file = AppSingleFileField(upload_to="files/event/image/")

class Event(BaseModel):
   title = models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
   status =AppSingleChoiceField(choices_config=STATUS,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
   description = models.TextField()
   point =models.IntegerField()
   date = models.DateTimeField()


   def __str__(self):
       return self.title