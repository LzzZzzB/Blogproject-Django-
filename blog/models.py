# coding: utf-8
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User #教程没有加这句 无法迁移数据库 因为找不到User (原来是我抄漏了)
from django.utils.six import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class Category(models.Model):      #文章分类
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=100)

    body = models.TextField()

    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def Meta(self):
        ordering = ['-created_time', 'title']