"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from authentication import views as auth_views
from author import views as author_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/register/', auth_views.register_view, name='register'),
    path('auth/login/', auth_views.login_view, name='login'),
    path('auth/logout/', auth_views.logout_view, name='logout'),

    path('users/', auth_views.user_list, name='user_list'),
    path('users/<int:user_id>/', auth_views.user_detail, name='user_detail'),

    path('authors/', author_views.author_list, name='author_list'),
    path('authors/create/', author_views.author_create, name='author_create'),
    path('authors/delete/<int:author_id>/', author_views.author_delete, name='author_delete'),
]


