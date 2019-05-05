from django.contrib import admin

# Register your models here.
from accounts.models import Profile, Dog

admin.site.register(Profile)
admin.site.register(Dog)
