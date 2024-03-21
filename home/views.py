from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Review
from django.core.paginator import Paginator
from .forms import ReviewForm

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
    
    # Review form
    if request.method == 'POST':
        print("es post")
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            cf = review_form.cleaned_data
            Review.objects.create(
                post=post,
                author = cf['author'],
                text= cf['text'],
                rating= cf['rating'],
            )
            print("se creo")
            
        return redirect('home:post_detail', slug=post.slug)
    
    else:
        review_form = ReviewForm
    
    context = {'post':post, 'review_form': review_form}
    return render(request, 'home/detail.html', context)
    