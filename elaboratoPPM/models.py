from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

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

class Category(models.Model):
    name = models.CharField(max_length=255, choices=choice_list, unique=True)

    def get_absolute_url(self):
        return reverse('home')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Category, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    età = models.IntegerField(null=True, blank=True)
    città = models.CharField(max_length=255, null=True, blank=True)
    hobby = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField()
    website_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')



class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, choices= CATEGORY_CHOICES, default='blog')
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.author)
