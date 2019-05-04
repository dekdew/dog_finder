from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
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


def my_login(req):
    context={}
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(req, username=username, password=password)

        if user:
            login(req, user)
            next_url = req.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            return redirect('index')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong Username or Password'

    next_url = req.GET.get('next')
    if next_url:
        context['next_url'] = next_url
    return render(req, 'accounts/login.html', context)


def my_logout(req):
    logout(req)
    return redirect('index')


@login_required
def profile(req):

    return render(req, 'accounts/profile.html')
