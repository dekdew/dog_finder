from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from accounts.models import Profile


class UserRegisterForms(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class UserUpdateForms(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    owner_phone = forms.CharField(max_length=20)
    owner_address = forms.Textarea()

    class Meta:
        model = Profile
        fields = ['owner_phone', 'owner_address', 'image']
