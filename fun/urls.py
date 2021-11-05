from django.urls import path
from . import views

urlpatterns = [
    path('', views.fun_index, name='fun'),
]