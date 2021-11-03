from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import CustomUserCreationForm
from resume.resume_data import *
from blog.models import Post


def dashboard(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'projects': projects,
        'experience': experience,
        'skills': skills,
        'skill_list': skill_list,
        "posts": posts,
    }
    return render(request, "users/dashboard.html", context)

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()
            login(request, user)
            return redirect(reverse("dashboard"))