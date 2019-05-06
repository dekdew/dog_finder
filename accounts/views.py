from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import UserRegisterForms, UserUpdateForms, ProfileUpdateForm, DogRegisterForms
from accounts.models import Breed, DogColor


def register(req):
    if req.method == 'POST':
        form = UserRegisterForms(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(req, f'Account created for {username}')

            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(req, new_user)

            return redirect('edit_profile')
    else:
        form = UserRegisterForms()

    return render(req, 'accounts/register.html', {'form': form})


@login_required
def register_dog(req):
    if req.method == 'POST':
        dog_form = DogRegisterForms(req.POST)
        if dog_form.is_valid():
            dog = dog_form.save(commit=False)
            dog.owner = req.user
            dog_form.save()
            return redirect('my_profile')
    else:
        dog_form = DogRegisterForms()
    context = {'dog_form': dog_form}
    return render(req, 'accounts/dog_register.html', context)

def my_login(req):
    context = {}
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(req, username=username, password=password)

        if user:
            login(req, user)
            next_url = req.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            return redirect('my_profile')
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
def edit_profile(req):
    if req.method == 'POST':
        user_form = UserUpdateForms(req.POST, instance=req.user)
        profile_form = ProfileUpdateForm(req.POST, req.FILES, instance=req.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(req, f'Your account has been update!')
            return redirect('my_profile')
    else:
        user_form = UserUpdateForms(instance=req.user)
        profile_form = ProfileUpdateForm(instance=req.user.profile)
        storage = messages.get_messages(req)
        storage.used = True

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(req, 'accounts/edit-profile.html', context=context)


@login_required
def my_profile(req):
    if req.method == 'POST':
        pass
    else:
        pass

    context = {

    }
    return render(req, 'accounts/my-profile.html', context=context)
