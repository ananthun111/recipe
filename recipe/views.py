from django.shortcuts import render
from django.views import generic
from .models import Post
from django.db.models import Q

# Create your views here.
def home(request):
    search_post = request.GET.get('search')
    if search_post:
        post = Post.objects.filter(Q(title__icontains=search_post) | Q(meta_description__icontains=search_post)).filter(status=3)
    else:
        post = Post.objects.filter(status=3).order_by('-updated_on')[:10]
    # print(post[0])
    return render(request, 'home.html',{'posts':post})
def coming(request):
    return render(request, 'comingsoon.html')

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(status=3).order_by('-updated_on')[:10]
        return context