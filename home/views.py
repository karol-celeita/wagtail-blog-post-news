from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Review, Categories
from django.core.paginator import Paginator
from .forms import ReviewForm, SearchForm
from django.contrib.postgres.search import SearchVector,SearchQuery, SearchRank
from taggit.models import Tag

#List View

def post_list(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    categories = Categories.objects.all()
    #Pagination
    post_per_page = 3
    paginator = Paginator(posts, post_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'page_obj':page_obj, "tags":tags, "categories":categories}
    return render(request, 'home/index.html', context)

# post_detail
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug,)
    tags = Tag.objects.all()
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
    
    context = {'post':post, 'review_form': review_form, "tags":tags}
    return render(request, 'home/detail.html', context)


def post_filter(request, category_slug=None, tag_slug=None):
    
    posts = Post.objects.all()
    categories = Categories.objects.all()
    tags = Tag.objects.all() 
    
    # category_filter
    requested_category = None
    if category_slug:
        requested_category = get_object_or_404(Categories, slug=category_slug)
        posts = posts.filter(category__in=[requested_category])
        
    #tag filter
    requested_tag = None
    if tag_slug:
        requested_tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[requested_tag])
        
    post_per_page = 5
    paginator = Paginator(posts, post_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {"categories":categories, "tags":tags, "page_obj":page_obj}
    return render(request, 'home/filters.html', context)


def post_search(request):
    form = SearchForm()
    query = None
    results = []
    categories = Categories.objects.all()
    tags = Tag.objects.all() 
    
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid:
            query = form.cleaned_data['query']
            search_vector = SearchVector('title', 'body')
            search_query = SearchQuery(query, config='English')
            results = Post.objects.annotate(
                search = search_vector, rank= SearchRank(search_vector, search_query)).filter(search = search_query).order_by('-rank')
            
    post_per_page = 5
    paginator = Paginator(results, post_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {"categories":categories, "tags":tags, "page_obj":page_obj}
    return render( request, 'home/post_search.html', context )