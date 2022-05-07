
from django.contrib import admin
from django.urls import path
from .views import posts_of_following_profile

app_name = 'post'

urlpatterns = [
    path('', posts_of_following_profile, name='all_following_post'),
]
