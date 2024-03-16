from django.shortcuts import render, get_object_or_404
from .models import Post

#List View

def post_list(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'home/index.html', context)

# post_detail
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug,)
    context = {'post':post}
    return render(request, 'home/detail.html', context)
    