from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from .models import Women


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]
data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': '''<h1>Анджелина Джоли</h1> (англ. Angelina Jolie[7], при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.
    Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».''',
     'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]

cats_db = [
    {'id':1, 'name':'Acress'},
    {'id':2, 'name':'Singers'},
    {'id':3, 'name':'Sportswomen'},
]


def index(request):
    posts = Women.published.all()
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

def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")

def show_category(request, cat_id):
    
    data = {
    'title': 'Главная страница',
    'menu': menu,
    'posts':data_db,
    'cats_selected':cat_id
    }
    
    return render(request, 'women/index.html', context=data)

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")