from django.urls import path

from newfeeds import views
from newfeeds.views import PostListView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post/new/', PostCreateView.as_view(), name='create-post'),
    path('about/', views.about, name='about'),

]