from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from apps.BASE.managers import UserManager
from apps.BASE.models import (
    BaseModel,
    MAX_CHAR_FIELD_LENGTH,
    DEFAULT_BLANK_NULLABLE_FIELD_CONFIG,
)


# Custom User Model
class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    email = models.CharField(
        max_length=150, unique=True, **DEFAULT_BLANK_NULLABLE_FIELD_CONFIG
    )
    full_name = models.CharField(
        max_length=MAX_CHAR_FIELD_LENGTH, **DEFAULT_BLANK_NULLABLE_FIELD_CONFIG
    )
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return f"{self.email} ({self.full_name})"
