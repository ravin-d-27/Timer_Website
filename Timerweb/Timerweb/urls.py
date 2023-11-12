"""
URL configuration for Timerweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from Timer import views
from accounts import views as acviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('new_timer/', views.new_timer, name='new_timer'),
    path('start_timer/<int:timer_id>/', views.start_timer, name='start_timer'),
    path('new_timer2/', views.new_timer2, name='new_timer2'),
    path('start_timer2/<int:timer_id>/', views.start_timer2, name='start_timer2'),
    path('login/', acviews.login, name='login'),
    path('signup/', acviews.signup, name='signup'),
    path('logout/', acviews.logout, name='logout'),
    path('elapsed_time/', views.elapsed_time, name='elapsed_time'),
    path('display/', views.display_people, name='display'),
    path('clear/', views.clear, name='clear'),
]
