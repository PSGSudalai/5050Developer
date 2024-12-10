from apps.BASE.model_fields import AppSingleChoiceField, AppSingleFileField
from apps.BASE.models import DEFAULT_BLANK_NULLABLE_FIELD_CONFIG, MAX_CHAR_FIELD_LENGTH, BaseModel
from django.db import models

from apps.HELPERS.choices import STATUS

class EventImage(BaseModel):
    file = AppSingleFileField(upload_to="files/event/image/")

class DemoVideo(BaseModel):
    file = AppSingleFileField(upload_to="files/event/demo-video/")

class Event(BaseModel):
   image=models.ForeignKey(EventImage,on_delete=models.SET_NULL,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
   title = models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
   status =AppSingleChoiceField(choices_config=STATUS,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
   description = models.TextField(**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
   point =models.IntegerField(**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
   date = models.DateField(**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
   start_time = models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
   end_time = models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
   amount = models.IntegerField(**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
   about = models.TextField(**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
   video = models.ForeignKey(DemoVideo,on_delete=models.SET_NULL,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
   keyskill = models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
  


   def __str__(self):
       return self.title