from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from newfeeds.models import Post


def index(req):
    context = {'posts': Post.objects.all()}
    return render(req, 'newfeeds/index.html', context=context)

def about(req):

    return render(req, 'newfeeds/about.html', {'title': 'Post About'})
