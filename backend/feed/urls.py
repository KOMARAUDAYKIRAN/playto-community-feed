from django.urls import path
from . import views

urlpatterns = [
    path('feed/', views.feed),
    path('like/post/<int:post_id>/', views.like_post),
    path('leaderboard/', views.leaderboard),
]
