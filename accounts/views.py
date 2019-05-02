from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def register(req):
    form = UserCreationForm()
    return render(req, 'accounts/register.html', {'form': form})

