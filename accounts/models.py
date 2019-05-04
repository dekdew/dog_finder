from PIL import Image
from django.contrib.auth.models import User
from django.db import models

# Create your models here


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_img')
    owner_phone = models.CharField(max_length=20, default='08x-xxx-xxxx')
    owner_address = models.TextField(default='default Address')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        print(self.image.path)
        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)


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
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


class DogColor(models.Model):
    color_name = models.CharField(max_length=30)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, null=True)

