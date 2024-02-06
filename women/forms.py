from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator

from .models import Category, Husband,Women


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Women
        fields = '__all__'
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-input'}),
            'content':forms.Textarea(attrs={'cols':50, 'rows':5})
        }

        labels = {
            'slug':'URL'
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) >20:
            raise ValidationError('No more than 20 characters')
        return title


class UploadFileForm(forms.Form):
    file = forms.ImageField(label='Select a file')





#
# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255,min_length=5,
#                             label='Title',
#                             widget=forms.TextInput(attrs={'class':'form-input'}),
#                             error_messages={'min_length':'Title must be at least 5 characters.','required':'Please enter a title.'}
#                             )
#     slug = forms.SlugField(max_length=255, label='URL',
#                            validators=[MinLengthValidator(5), MaxLengthValidator(100)])
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols':50, 'rows':5}),label='Content',required=False)
#     is_published = forms.BooleanField(label='Status', initial=True)
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Category')
#     husband = forms.ModelChoiceField(queryset=Husband.objects.all(), label='Husband',required=False)