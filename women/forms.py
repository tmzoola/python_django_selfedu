from django import forms
from .models import Category, Husband


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label='Title', widget=forms.TextInput(attrs={'class':'form-input'}))
    slug = forms.SlugField(max_length=255, label='URL')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':50, 'rows':5}),label='Content',required=False)
    is_published = forms.BooleanField(label='Status', initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Category')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), label='Husband',required=False)