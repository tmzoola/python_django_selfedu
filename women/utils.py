menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]
class DataMixin:
    title_page = None
    cats_selected = None
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page
        if self.cats_selected is not None:
            self.extra_context['cats_selected'] = self.cats_selected
        if "menu" not in self.extra_context:
            self.extra_context["menu"]=menu

    def get_mixin_context_data(self,context, **kwargs):
        context['menu'] = menu
        context['cat_selected'] =None
        context.update(kwargs)
        return context