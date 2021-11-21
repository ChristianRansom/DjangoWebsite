from django.conf.urls import url, include
from users.views import dashboard, register, user_settings
from . import views


urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^register/", register, name="register"),
    url(r"^oauth/", include("social_django.urls")),
    url(r"^user_settings/", user_settings, name="user_settings"),
    url(r'^google-login/$', views.google_login, name="google_login"),
    url('', include('social_django.urls', namespace='social'))
]