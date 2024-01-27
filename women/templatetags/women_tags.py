from django import template
import women.views as views


register = template.Library()

@register.simple_tag(name='getcats')
def get_categories():
    return views.cats_db


@register.inclusion_tag('women/list_categories.html')
def show_categories(cats_selected=0):
    cats = views.cats_db
    return {'cats':cats,'cats_selected':cats_selected}