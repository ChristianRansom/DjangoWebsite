from django.urls import path
from . import views

urlpatterns = [
    path("", views.resume_index, name="resume_index"),
    path("project/<int:pk>/", views.project_detail, name="project_detail"),
    path("download/<str:path>/", views.download, name="download"),
]