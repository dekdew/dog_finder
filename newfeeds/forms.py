from django import forms
from django.forms import ModelChoiceField

from accounts.models import Dog
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
