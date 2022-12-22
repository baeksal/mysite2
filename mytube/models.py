from django.db import models
from django.contrib.auth.models import User
import os

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=200, unique=True,  allow_unicode=True)
    description = models.TextField(default='카테고리 설명')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/mytube/category/{self.slug}/'

class Post(models.Model):
    title = models.CharField(max_length=100)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, blank=True) #다대다 #카테고리 중복 선택 

    video_id = models.CharField(max_length=50, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='1')

    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/mytube/{self.pk}/'

