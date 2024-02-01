from django.contrib import admin
from .models import Women,TagPost,Category,Husband
# Register your models here.


class MarriedFilter(admin.SimpleListFilter):
    title = 'Marriage status'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [('married','Married'),('single','Single')]
    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull=True)
@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'cat','husband','tags','slug']
    filter_horizontal = ['tags']
    list_display=('id', 'title', 'time_create', 'is_published','cat')
    list_display_links=('id', 'title')
    ordering=['time_create','title']
    list_editable=['is_published']
    list_per_page = 10
    search_fields = ['title','cat__name']
    list_filter = [MarriedFilter,'cat__name','is_published']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','name')
    list_display_links=('id','name')

