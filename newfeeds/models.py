from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from accounts.models import Dog, DogFound

MALE, FEMALE = 'Male', 'Female'

GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )


class Post(models.Model):
    date = models.DateTimeField(default=timezone.now)
    post_title = models.CharField(max_length=100)
    post_detail = models.TextField()

    NFOUND, FOUND = '0', '1'
    STATUS = (
        (NFOUND, '0'),
        (FOUND, '1')
    )

    post_status = models.CharField(choices=STATUS, null=False, blank=False, max_length=2)
    latitude = models.FloatField()
    longtitude = models.FloatField()

    DOG_LOST, DOG_FOUND = '0', '1'
    TYPES = (
        (DOG_LOST, '0'),
        (DOG_FOUND, '1')
    )
    types = models.CharField(choices=TYPES, null=False, blank=False, max_length=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, null=True)
    founder = models.ForeignKey(DogFound, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.post_title


# class DogFound(models.Model):
#     founder_name = models.CharField(max_length=50)
#     founder_info = models.TextField()
#     founder_phone = models.CharField(max_length=20)
#
#     dog_gender = models.CharField(choices=GENDER, default='Male', max_length=10)
#     post = models.OneToOneField(Post, on_delete=models.CASCADE, primary_key=True)
#
#
#
# class DogLost(models.Model):
#     post = models.OneToOneField(Post, on_delete=models.CASCADE, primary_key=True)
#     dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
#
#

# class Comment(models.Model):
#     date_time = models.DateTimeField(auto_now_add=True)