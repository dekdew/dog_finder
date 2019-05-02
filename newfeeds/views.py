from django.http import HttpResponse
from django.shortcuts import render


posts = [
    {
        'owner': 'Khing',
        'post_title': 'Blog1',
        'post_detail': 'First Post Content',
        'date_time': 'August 28, 2019'
    },
{
        'owner': 'Khing2',
        'post_title': 'Blog2',
        'post_detail': 'Second Post Content',
        'date_time': 'August 29, 2019'
    }
]

# Create your views here.
def index(req):
    context = {'posts': posts}
    return render(req, 'newfeeds/index.html', context=context)

def post(req):

    return render(req, 'newfeeds/post.html', {'title': 'Post About'})
