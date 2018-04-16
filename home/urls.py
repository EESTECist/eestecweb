from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name="index"),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name="postdetail"),
    #path('posts/<int:post_id>/', views.PostListView.as_view(), name="list"),
]
