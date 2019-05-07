from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView

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


class PostCreateView(CreateView):
    model = Post
    template_name = 'newfeeds/post-create.html'
    fields = ['post_title', 'post_detail', 'latitude', 'longtitude']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


def about(req):

    return render(req, 'newfeeds/about.html', {'title': 'Post About'})


def post(req):
    return render(req, 'newfeeds/post.html', {'title': 'Post About'})

