from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView

from .forms import AddPostForm, UploadFileForm
from .models import Category, TagPost, Women, UploadFiles
from .utils import DataMixin


class WomenHome(DataMixin,ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    title_page ='Главная страница'
    cats_selected = 0
    def get_queryset(self):
        return Women.published.all().select_related('cat')


def about(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()
    else:
        form = UploadFileForm()
    data = {
    'title': 'About page',
    'form':form
    }
    
    return render(request, 'women/about.html', context=data)



class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context_data(context, title=context['post'].title)

    def get_object(self):
        return get_object_or_404(Women.published, slug=self.kwargs[self.slug_url_kwarg])

class WomenTagList(DataMixin,ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return Women.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')

    def context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagPost.objects.get(slug=self.kwargs['tag_slug'])
        return self.get_mixin_context_data(context, title=f"Tag: {tag.tag}")

class WomenCategory(DataMixin,ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False
    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat  = context['posts'][0].cat
        return self.get_mixin_context_data(context, title=f'Category {cat.name}', cats_selected=cat.pk)

class AddPage(DataMixin,CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    title_page = 'Add Page'
class UpdatePage(DataMixin,UpdateView):
    model = Women
    fields = "__all__"
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    title_page = 'Update Page'



def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")