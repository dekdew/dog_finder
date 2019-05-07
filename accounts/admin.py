from django.contrib import admin
from django.contrib.auth.models import Permission
# Register your models here.
from accounts.models import Profile, Dog

admin.site.register(Permission)

admin.site.register(Profile)
admin.site.register(Dog)
