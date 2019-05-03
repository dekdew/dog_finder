from django.contrib.auth.models import User
from django.db import models

# Create your models here


class Owner(models.Model):
    owner_phone = models.CharField(max_length=15)
    owner_address = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Dog(models.Model):

    MALE, FEMALE = 'Male', 'Female'
    GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )

    DEATH, NORMAL, LOST = 'Death', 'Normal', 'Lost'
    STATUS = (
        (DEATH, 'Death'),
        (NORMAL, 'Normal'),
        (LOST, 'Lost')
    )

    dog_status = models.CharField(choices=STATUS, default='Normal', max_length=20)
    dog_name = models.CharField(max_length=50)
    dog_info = models.TextField()

    dog_gender = models.CharField(choices=GENDER, default='Male', max_length=10)
    dog_dob = models.DateField(null=True, blank=True)
    dog_age = models.IntegerField(default=0)
    qr_code = models.TextField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)