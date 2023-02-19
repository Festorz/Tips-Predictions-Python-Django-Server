import random
import string
from django.db import models
from django.conf import settings
from django.utils.text import slugify


# Create your models here.


def create_slug_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        blank=True, null=True)
    slug = models.SlugField(default='', null=False, editable=False)
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='blog-images', default='')
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='likes', blank=True, editable=False)
    views = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='views', blank=True, editable=False)
    intro = models.TextField(default='')
    body = models.TextField(default='')
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def number_of_views(self):
        return self.views.count()

    class Meta:
        ordering = ['-date_added']

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.TextField(default='')
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date_added']
