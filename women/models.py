from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)


class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Not Published'
        PUBLISHED = 1, 'Published'
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    time_create = models.DateField(auto_now_add=True)
    time_update = models.DateField(auto_now=True)
    is_published = models.BooleanField(choices = Status.choices, default=Status.PUBLISHED)
    cat = models.ForeignKey('Category', on_delete = models.PROTECT, related_name='posts')
    tags = models.ManyToManyField('TagPost', related_name="tags",blank=True)
    husband = models.OneToOneField('Husband', on_delete=models.SET_NULL, null = True, blank = True,related_name='wuman')
    
    objects = models.Manager()
    published = PublishedManager()
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-time_create']
        
        indexes = [
            models.Index(fields=['-time_create'])
        ]
        
    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index = True)
    slug = models.SlugField(max_length=255, unique=True, db_index = True)
    
    
    def __str__(self) -> str:
        return self.name
    
class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, db_index = True,unique=True)
    
    
    def __str__(self) -> str:
        return self.tag

class Husband(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    m_count = models.IntegerField(blank=True, default=0)
    def __str__(self) -> str:
        return self.name