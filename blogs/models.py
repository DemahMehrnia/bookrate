import uuid

from django.db import models
from main_moudles.models import bookcategory,Books
from account.models import User
from django.utils.text import slugify
# Create your models here.

class blogs(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blogauthor', null=True)
    content = models.TextField()
    short_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to='images',null=True,blank=True)
    likes = models.ManyToManyField(User, related_name='bloglikes',blank=True)
    dislike = models.ManyToManyField(User, related_name='blogdislikes',blank=True)
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
        except:pass
