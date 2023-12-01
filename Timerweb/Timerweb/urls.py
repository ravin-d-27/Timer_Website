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
    path('elapsed_time2/', views.elapsed_time2, name='elapsed_time2'),
    path('new_timer3/', views.new_timer3, name='new_timer3'),
    path('start_timer3/<int:timer_id>/', views.start_timer3, name='start_timer3'),
    path('start_timer3a/<int:timer_id>/', views.start_timer3a, name='start_timer3a'),
    path('elapsed_time3/', views.elapsed_time3, name='elapsed_time3'),
    path('elapsed_time3a/', views.elapsed_time3a, name='elapsed_time3a'),
    path('credits/', views.credits, name='credits'),
]
