from django import forms
from django.forms import ModelChoiceField

from accounts.forms import BreedModelChoiceField, DogColorModelChoiceField
from accounts.models import Dog, Breed, DogColor, DogFound
from newfeeds.models import Post


class DogModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.dog_name


class PostModelForm(forms.ModelForm):
    dog_name = DogModelChoiceField(queryset=Dog.objects.none(), to_field_name='dog_name')
    latitude = forms.CharField(widget = forms.TextInput(attrs={'readonly':'readonly'}))
    longtitude = forms.CharField(widget = forms.TextInput(attrs={'readonly':'readonly'}))

    class Meta:
        model = Post
        fields = ['post_title', 'post_detail', 'dog_name', 'latitude', 'longtitude']
        exclude = ['owner', 'dog', 'post_status', 'types']

    def __init__(self, user, *args, **kwargs):
        super(PostModelForm, self).__init__(*args, **kwargs)
        self.fields['dog_name'].queryset = Dog.objects.filter(owner=user)


class PostFoundModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['latitude', 'longtitude']
        exclude = ['post_status', 'types']


class FounderModelForm(forms.ModelForm):
    dog_breed = BreedModelChoiceField(queryset=Breed.objects.all(), to_field_name="breed_name")
    dog_color = DogColorModelChoiceField(queryset=DogColor.objects.all(), to_field_name="color_name")

    class Meta:
        model = DogFound
        fields = ['founder_name', 'founder_info', 'founder_phone', 'dog_gender', 'dog_color', 'dog_breed', 'dog_image']