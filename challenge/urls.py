from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.register_challenge, name = "register_challenge"),
    path('list', views.find_challenge_list, name = "find_challenges"),
    path('<int:challenge_id>', views.challenge_detail_feed),
]