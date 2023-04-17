
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_post", views.new_post, name="new_post"),
    path("user/<int:profile_id>", views.profile, name="profile_id"),
    path("user/<int:followed_id>/follow", views.follow, name="followed_id"),
    path("user/<int:unfollowed_id>/unfollow", views.unfollow, name="unfollowed_id"),
    path("following", views.following_page, name="following"),
    path("edit/<int:id>", views.edit, name="id"),
    path("like/<int:id>", views.like, name="id"),
    path("posts", views.liked_posts, name="posts"),
]
