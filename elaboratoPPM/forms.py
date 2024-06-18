from django import forms
from .models import Post, Category, Comment

CATEGORY_CHOICES= [
    ('blog', 'blog'),
    ('esami', 'esami'),
    ('libri/appunti','libri/appunti'),
    ('news','news'),
    ('ripetizioni','ripetizioni'),
]

choice_list = []

for item in CATEGORY_CHOICES:
    if item not in choice_list:
        choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'elder', 'type':'hidden' }),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'id': 'cats'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'body')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }