from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator


#List View

def post_list(request):
    posts = Post.objects.all()
    
    #Pagination
    post_per_page = 3
    paginator = Paginator(posts, post_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'page_obj':page_obj}
    return render(request, 'home/index.html', context)

# post_detail
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug,)
    context = {'post':post}
    return render(request, 'home/detail.html', context)
    