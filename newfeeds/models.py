from django.db import models


MALE, FEMALE = 'Male', 'Female'

GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )




#
# class Post(models.Model):
#     date_time = models.DateTimeField(auto_now_add=True)
#     post_detail = models.TextField()
#
#     NFOUND, FOUND = 0, 1
#     STATUS = (
#         (NFOUND, 0),
#         (FOUND, 1)
#     )
#
#     post_status = models.CharField(choices=STATUS, null=False, blank=False, max_length=2)
#     latitude = models.FloatField()
#     longtitude = models.FloatField()
#
#     DOG_LOST, DOG_FOUND = 0, 1
#     TYPES = (
#         (DOG_LOST, 0),
#         (DOG_FOUND, 1)
#     )
#     types = models.CharField(choices=TYPES, null=False, blank=False, max_length=2)
#     owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
#
#
# class DogFound(models.Model):
#     founder_name = models.CharField(max_length=50)
#     founder_info = models.TextField()
#     founder_phone = models.CharField(max_length=20)
#
#     dog_gender = models.CharField(choices=GENDER, default='Male', max_length=10)
#     post = models.OneToOneField(Post, on_delete=models.CASCADE, primary_key=True)
#
#
# class Dog(models.Model):
#
#     DEATH, NORMAL, LOST = 'Death', 'Normal', 'Lost'
#     STATUS = (
#         (DEATH, 'Death'),
#         (NORMAL, 'Normal'),
#         (LOST, 'Lost')
#     )
#
#     dog_status = models.CharField(choices=STATUS, default='Normal', max_length=20)
#     dog_name = models.CharField(max_length=50)
#     dog_info = models.TextField()
#
#     dog_gender = models.CharField(choices=GENDER, default='Male', max_length=10)
#     dog_dob = models.DateField(null=True, blank=True)
#     dog_age = models.IntegerField(default=0)
#     qrcode = models.TextField()
#
#
# class DogLost(models.Model):
#     post = models.OneToOneField(Post, on_delete=models.CASCADE, primary_key=True)
#     dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
#
#
# class DogColor(models.Model):
#     color_name = models.CharField(max_length=30)
#     dog = models.ForeignKey(Dog, on_delete=models.CASCADE, null=True)
#     dog_found = models.ForeignKey(DogFound, on_delete=models.CASCADE, null=True)
#
#
# class Comment(models.Model):
#     date_time = models.DateTimeField(auto_now_add=True)