from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import CustomUserCreationForm
from resume.resume_data import *
from blog.models import Post
from django.contrib.auth.forms import UserCreationForm


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
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})