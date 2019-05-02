from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.


class Owner(AbstractBaseUser):
    email = models.EmailField(max_length=255,unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    name = models.CharField(max_length=255)
    owner_phone = models.CharField(max_length=15)
    owner_address = models.TextField()
