from django.urls import path
from . import views

app_name = 'home'
urlpatterns =[
    path('', views.post_list, name='post_list'),
    path('<slug:slug>', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', views.post_filter, name='category_filter'),
    path('tag/<slug:tag_slug>/', views.post_filter, name='tag_filter'),
    path('search/', views.post_search, name='search'),
]