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

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Breed(models.Model):
    PUG, HUSKY, CORGI = "Pug", "Siberian Husky", "Corgi"
    BREED = (
        (PUG, 'Pug'),
        (HUSKY, 'Siberian Husky'),
        (CORGI, 'Corgi')
    )
    breed_name = models.CharField(max_length=100)


class DogColor(models.Model):

    color_name = models.CharField(max_length=30)


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

    dog_name = models.CharField(max_length=50)
    dog_gender = models.CharField(choices=GENDER, default='Male', max_length=10)
    dog_breed = models.ForeignKey(Breed, on_delete=models.CASCADE, default=1)
    color1 = models.ForeignKey(DogColor, on_delete=models.CASCADE, default=1)
    dog_dob = models.DateField(null=True, blank=True)
    dog_info = models.TextField(default='-')
    dog_age = models.IntegerField(default=0)
    dog_image = models.ImageField(default='default-dog.jpg', upload_to='dog_img')
    qr_code = models.TextField(default='-')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    dog_status = models.CharField(choices=STATUS, default='Normal', max_length=20)


    def __str__(self):
        return f'{self.owner.username} {self.dog_name} Profile'

    def save(self, *args, **kwargs):
        super(Dog, self).save(*args, **kwargs)

        img = Image.open(self.dog_image.path)

        if img.height > 500 or img.width > 700:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.dog_image.path)


