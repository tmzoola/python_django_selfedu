from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from .models import Category, TagPost, Women


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]


def index(request):
    posts = Women.published.all().select_related('cat')
    data = {
    'title': 'Главная страница',
    'menu': menu,
    'posts':posts,
    'cats_selected':0
    }
    return render(request, 'women/index.html', context=data)

def about(request): 
    data = {
    'title': 'About page',
    'menu': menu,
    'posts':data_db
    }
    
    return render(request, 'women/about.html', context=data)


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    
    data = {
        'title':post.title,
        'menu':menu,
        'post':post,
        'cats_selected':1
    }
    
    return render(request, 'women/post.html', data)

def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Women.Status.PUBLISHED).select_related('cat')

    
    data = {
        'title':f"Tag: {tag.tag}",
        'menu':menu,
        'posts':posts,
        'cats_selected':None,
    }

    
    return render(request, 'women/index.html', context=data)

def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    
    posts = Women.objects.filter(cat_id=category.pk).select_related('cat')
    
    data = {
    'title': f'Category {category.name}',
    'menu': menu,
    'posts':posts,
    'cats_selected':category.pk
    }
    
    return render(request, 'women/index.html', context=data)

def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")