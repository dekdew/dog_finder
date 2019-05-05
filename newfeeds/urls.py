from django.urls import path

from newfeeds import views
from newfeeds.views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('about/', views.about, name='about'),

]