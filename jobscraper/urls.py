from django.urls import path
from . import views

urlpatterns = [
    path("", views.job_scraper, name="job_scraper"),
]