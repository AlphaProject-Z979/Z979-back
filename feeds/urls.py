from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('list/<int:user_id>', views.find_my_feed, name="find_my_feed"), # 내 글 모아보기
    path('<int:user_id>',views.post_feed, name="post_feed"),
    path('<int:user_id>/<int:feed_id>',views.update_feed, name="update_feed"),
    path('list',views.all_feed_list, name="find_all_feed"),
    path('<int:feed_id>',views.like_feed, name="like_feed"), # 좋아요 누르기
    path('list/challenges',views.find_challenge_feed, name="find_challenge_feed"),
    path('<int:challenge_id>/best',views.find_challenge_feed_orderby_like, name="find_challenge_feed"),
]