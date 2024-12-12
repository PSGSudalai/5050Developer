from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from apps.BASE.managers import UserManager
from apps.BASE.model_fields import AppSingleChoiceField
from apps.BASE.models import (
    BaseModel,
    MAX_CHAR_FIELD_LENGTH,
    DEFAULT_BLANK_NULLABLE_FIELD_CONFIG,
)
from apps.HELPERS.choices import ATTENDANCE


# Custom User Model
class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    student_id = models.CharField(
        max_length=MAX_CHAR_FIELD_LENGTH, **DEFAULT_BLANK_NULLABLE_FIELD_CONFIG
    )
    email = models.CharField(
        max_length=150, unique=True, **DEFAULT_BLANK_NULLABLE_FIELD_CONFIG
    )
    name = models.CharField(
        max_length=MAX_CHAR_FIELD_LENGTH, **DEFAULT_BLANK_NULLABLE_FIELD_CONFIG
    )
    phone = models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    college_name = models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    address = models.TextField(**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    dob = models.DateField(**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    point = models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    certificate = models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,**DEFAULT_BLANK_NULLABLE_FIELD_CONFIG)
    status = AppSingleChoiceField(choices_config=ATTENDANCE,default="Present")

    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    
    def save(self, *args, **kwargs):
        # Auto-generate student_id if not set
        if not self.student_id:
            last_student = User.objects.all().order_by("id").last()
            if last_student and last_student.student_id:
                last_student_id = last_student.student_id
                try:
                    user_number = int(last_student_id.split("RS")[-1]) + 1
                except ValueError:
                    user_number = 1  # Fallback in case of unexpected ID format
                self.student_id = f"RS{user_number:04d}"
            else:
                self.student_id = "RS0001"

        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.email} ({self.name})"
