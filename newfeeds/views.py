from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView


from accounts.models import Dog, DogFound, Breed, DogColor
from newfeeds.forms import PostModelForm, PostFoundModelForm, FounderModelForm

post_list = [
    {
        'owner': 'Khing',
        'dog_name': 'Tommy',
        'date': 'August 28, 2019',
        'image': 'demo-image-01',
        'breed': 'Dachshund',
        'gender': 'male',
        'age': 2,
        'colors': [
            'black',
            'brown',
        ],
        'lat': '13.729896',
        'lon': '100.779320',
        'location': 'Kmitl',
    },
    {
        'owner': 'Few',
        'dog_name': 'Apple',
        'post_title': 'Blog2',
        'post_detail': 'Second Post Content',
        'date': 'August 29, 2019',
        'image': 'demo-image-02',
        'breed': 'Corgi',
        'gender': 'female',
        'age': 1,
        'colors': [
            'brown',
            'white',
        ],
        'lat': '6.999079',
        'lon': '100.472488',
        'location': 'Hadyai',
    }
]

# Create your views here.
from newfeeds.models import Post


def index(req):
    context = {'post_list': post_list}
    return render(req, 'newfeeds/index.html', context=context)


#
#     context = {'posts': Post.objects.all()}
#     return render(req, 'newfeeds/index.html', context=context)


class PostListView(ListView):
    model = Post
    template_name = 'newfeeds/index.html'
    context_object_name = 'posts'
    ordering = ['-date']


def matching(req):
    gender = 'Male'
    breed = 27
    color = 1

    dog_found = DogFound.objects.filter(dog_gender=gender).filter(dog_color=color).filter(dog_breed=breed)
    print(dog_found)
    return redirect('index')



@login_required
def create_post(req):
    if req.method == 'POST':
        form = PostModelForm(req.user, req.POST)
        if form.is_valid():
            post_form = form.save(commit=False)
            post_form.owner = req.user
            print('eiei  ' + str(form.cleaned_data.get('dog_name').dog_name))
            Dog.objects.filter(dog_name=form.cleaned_data.get('dog_name').dog_name, owner=req.user).update(
                dog_status='Lost')
            post_form.dog = Dog.objects.get(dog_name=form.cleaned_data.get('dog_name').dog_name)
            post_form.types = 0
            form.save()
            return redirect('index')
    else:

        form = PostModelForm(user=req.user)
    context = {'form': form}
    return render(req, 'newfeeds/post-create.html', context)


def create_found(req):
    if req.method == 'POST':
        post_form = PostFoundModelForm(req.POST)
        founder_form = FounderModelForm(req.POST, req.FILES)
        if post_form.is_valid() and founder_form.is_valid():
            p = post_form.save(commit=False)
            f = founder_form.save(commit=False)
            f.dog_breed = Breed.objects.get(breed_name=founder_form.cleaned_data.get('dog_breed').breed_name)
            f.dog_color = DogColor.objects.get(color_name=founder_form.cleaned_data.get('dog_color').color_name)

            f.save()
            p.types = 1
            p.founder = DogFound.objects.get(founder_name=founder_form.cleaned_data.get('founder_name'))
            post_form.save()
            founder_form.save()
            return redirect('index')
    else:

        post_form = PostFoundModelForm()
        founder_form = FounderModelForm()
    context = {'post_form': post_form, 'founder_form': founder_form}
    return render(req, 'newfeeds/post-found.html', context)

def about(req):
    return render(req, 'newfeeds/about.html', {'title': 'Post About'})


def post(req):
    return render(req, 'newfeeds/post.html', {'title': 'Post About'})
