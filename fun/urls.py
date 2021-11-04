from django.urls import path
from fun import views

urlpatterns = [
    path('', views.fun_index, name='fun_index'),
]