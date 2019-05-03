from django.contrib.auth.forms import UserCreationForm
from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from accounts.forms import UserRegisterForms


def register(req):
    if req.method == 'POST':
        form = UserRegisterForms(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(req, f'Account created for {username}')
            return redirect('index')
    else:
        form = UserRegisterForms()

    return render(req, 'accounts/register.html', {'form': form})

