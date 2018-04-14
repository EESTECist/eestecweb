from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def home(request):
    return render(request, 'home/homepage.html')

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'home/postdetail.html', {'post':post})
