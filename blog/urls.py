from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.allblogs ,name = 'allblogs'),
    path('hey', views.hey),
]
