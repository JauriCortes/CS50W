import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from django.contrib import messages
from django.views.decorators.csrf import  csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import Follows, Posts, User


def index(request):
    if request.user.is_authenticated:
        return render(request, "network/index.html", {
            "posts": Posts.objects.all()
        })
    
    else:
        return render(request, "network/index.html")

@csrf_exempt
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

@csrf_exempt
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html",{
            "message": "Welcome"
        })

@login_required
def new_post(request):

    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    user = request.user
    content = request.POST.get("content")

    post = Posts(
        poster = user,
        content = content
    )

    post.save()

    return HttpResponseRedirect(reverse("index"))

def profile(request, profile):

    profile_obj = User.objects.get(username=profile)
    followers = profile_obj.followers.all().count()
    following = profile_obj.following.all().count()

    b_name = "Follow"
    if request.user in profile_obj.followers.all():
        b_name = "Unfollow"

    posts = Posts.objects.filter(poster=profile_obj.id).reverse()
    
    return render(request, "network/profile.html", {
        "profile": profile_obj,
        "followers": followers,
        "following": following,
        "posts": posts,
        "b_name": b_name
    })

login_required
def follow_action(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    if request.POST.get("b_name") == "Follow":

        profile_n = request.POST.get(profile)
        print(f"followed {profile_n}")
