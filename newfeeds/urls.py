from django.urls import path

from newfeeds import views
from newfeeds.views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post/create/lost', views.create_post, name='post-create'),
    path('about/', views.about, name='about'),
    path('post/create/found', views.create_found, name='post-found'),
    path('hospital/', views.hospital, name='hospital'),

]