import datetime

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from accounts.models import Profile, Dog, Breed


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


class DogRegisterForms(forms.ModelForm):
    dog_name = forms.CharField(max_length=50)
    dog_gender = forms.ChoiceField(choices=Dog.GENDER)
    dog_dob = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    dog_age = forms.IntegerField()
    dog_breed = forms.ChoiceField(choices=Breed.BREED)
    dog_status = forms.ChoiceField(choices=Dog.STATUS)
    dog_info = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Dog
        fields = ['dog_image','dog_name', 'dog_gender', 'dog_breed', 'dog_dob', 'dog_age', 'dog_status', 'dog_info']

    def clean_dog_dob(self):
        data = self.cleaned_data['dog_dob']
        if data > datetime.date.today():
            raise forms.ValidationError('วันเกิิดสุนัขของท่านไม่ใช่วันในอดีต โปรดตรวจสอบวันเกิดสุนัขอีกครั้ง')

        print(data)
        return data
