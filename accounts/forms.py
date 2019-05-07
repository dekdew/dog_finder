import datetime

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelChoiceField
from django.contrib.auth.models import User

from accounts.models import Profile, Dog, Breed, DogColor


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


class BreedModelChoiceField(ModelChoiceField):
  def label_from_instance(self, obj):
    return "%s" % obj.breed_name


class DogColorModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.color_name


class DogRegisterForms(forms.ModelForm):

  dog_dob = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
  dog_breed = BreedModelChoiceField(queryset=Breed.objects.all(), to_field_name="breed_name")
  color1 = DogColorModelChoiceField(queryset=DogColor.objects.all(), to_field_name="color_name")

  class Meta:
    model = Dog
    fields = ['dog_name', 'dog_gender', 'dog_breed', 'color1', 'dog_dob', 'dog_info', 'dog_image']
    exclude = ['owner', 'dog_age', 'qr_code', 'dog_status']

  def clean_dog_dob(self):
    data = self.cleaned_data['dog_dob']
    if data > datetime.date.today():
      raise forms.ValidationError('วันเกิิดสุนัขของท่านไม่ใช่วันในอดีต โปรดตรวจสอบวันเกิดสุนัขอีกครั้ง')

    print(data)
    return data
