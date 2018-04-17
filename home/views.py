from django.shortcuts import render, get_object_or_404, Http404
from django.views import generic
from .models import Post

class PostListView(generic.ListView):
    model = Post
    context_object_name = 'post_list'
    queryset = Post.objects.filter()[:4]
    template_name = 'home/homepage.html'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'home/postdetail.html'
    def post_detail_view(request, pk):
        try:
            post_id = Post.objects.get(pk = pk)
        except Post.DoesNotExist:
            raise Http404("ops")

        return render(request, context={'post': post_id,})




#def home(request):
#    return render(request, 'home/homepage.html')
