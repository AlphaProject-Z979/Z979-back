from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/', views.find_my_stamps, name="find_my_stamps"), # 내 스탬프 조회

]