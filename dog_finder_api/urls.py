"""dog_finder_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('newfeeds.urls')),
    path('register/', accounts_views.register, name="register"),
    path('login/', accounts_views.my_login, name='login'),
    path('logout/', accounts_views.my_logout, name='logout'),
    path('my-profile/', accounts_views.my_profile, name='my_profile'),
    path('my-profile/edit/', accounts_views.edit_profile, name='edit_profile'),
    path('register/dog', accounts_views.register_dog, name='dog_register')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)