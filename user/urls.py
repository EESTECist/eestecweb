from django.urls import path
from .views import register, login_view, TeamCreateView, TeamPageView
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('create_team/', TeamCreateView.as_view(), name='team_create'),
    path('team/<slug:slug>/', TeamPageView.as_view(), name='team_page'),
    #path('logout/', auth_views.logout, name='logout'),
]