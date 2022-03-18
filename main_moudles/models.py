import uuid

from django.db import models
from account.models import User
from django.utils.text import slugify
# Create your models here.

class bookwriter(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField(null=True)
    image = models.FileField(upload_to='images', null=True,blank=True)
    slug = models.SlugField(default=uuid.uuid1,unique=True,allow_unicode=True,null=True,blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title,allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class bookcategory(models.Model):
    title = models.CharField(max_length=500,)
    slug = models.SlugField(default=uuid.uuid1,unique=True,allow_unicode=True,null=True,blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title,allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Books(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey(bookwriter, on_delete=models.CASCADE,related_name='authorrr', null=True)
    category = models.ManyToManyField(bookcategory,related_name='bookcat')
    image = models.FileField(upload_to='bookimages')
    short_description = models.CharField(max_length=300, null=True)
    likes = models.ManyToManyField(User, related_name='bookslikes', blank=True)
    dislike = models.ManyToManyField(User, related_name='booksdislikes', blank=True)
    readed = models.ManyToManyField(User, related_name='booksreaded', blank=True)
    reading = models.ManyToManyField(User, related_name='booksreading', blank=True)
    slug = models.SlugField(default=uuid.uuid1,unique=True,allow_unicode=True,null=True,blank=True)
    rate = models.IntegerField(null=True,blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title,allow_unicode=True)
        self.rate = self.rate_func()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}  {self.author}'

    def rate_func(self):
        try:
            a = self.likes.count()
            b = self.dislike.count()
            return int(a-b)
        except:
            pass
