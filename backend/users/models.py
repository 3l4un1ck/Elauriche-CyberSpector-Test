from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .manager import UserManager
from api.models import BaseModel


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    country = models.CharField(blank=True, null=True)
    phone_number = models.CharField(max_length=255, unique=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'first_name', 'last_name']

    objects = UserManager()

    class Meta:
        db_table = 'users'
