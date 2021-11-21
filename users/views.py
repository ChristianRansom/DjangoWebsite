from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import CustomUserCreationForm
from resume.resume_data import *
from blog.models import Post
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User


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
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def user_settings(request):
    return render(request, 'users/user_settings.html', {})


def google_login(request):
    redirect_uri = "%s://%s%s" % (
        request.scheme, request.get_host(), reverse('dashboard')
    )
    print(redirect_uri)
    if('code' in request.GET):
        params = {
            'grant_type': 'authorization_code',
            'code': request.GET.get('code'),
            'redirect_uri': redirect_uri,
            'client_id': settings.GP_CLIENT_ID,
            'client_secret': settings.GP_CLIENT_SECRET
        }
        url = 'https://accounts.google.com/o/oauth2/token'
        response = request.post(url, data=params)
        url = 'https://www.googleapis.com/oauth2/v1/userinfo'
        access_token = response.json().get('access_token')
        response = request.get(url, params={'access_token': access_token})
        user_data = response.json()
        email = user_data.get('email')
        if email:
            user, _ = User.objects.get_or_create(email=email, username=email)
            gender = user_data.get('gender', '').lower()
            if gender == 'male':
                gender = 'M'
            elif gender == 'female':
                gender = 'F'
            else:
                gender = 'O'
            data = {
                'first_name': user_data.get('name', '').split()[0],
                'last_name': user_data.get('family_name'),
                'google_avatar': user_data.get('picture'),
                'gender': gender,
                'is_active': True
            }
            user.__dict__.update(data)
            user.save()
            user.backend = settings.AUTHENTICATION_BACKENDS[0]
            login(request, user)
        else:
            messages.error(
                request,
                'Unable to login with Gmail Please try again'
            )
        return redirect('/')
    else:
        url = "https://accounts.google.com/o/oauth2/auth?client_id=%s&response_type=code&scope=%s&redirect_uri=%s&state=google"
        scope = [
            "https://www.googleapis.com/auth/userinfo.profile",
            "https://www.googleapis.com/auth/userinfo.email"
        ]
        scope = " ".join(scope)
        url = url % (settings.GP_CLIENT_ID, scope, redirect_uri)
        return redirect(url)
