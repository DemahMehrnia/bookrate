import uuid
from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import AbstractUser
from  django.utils import  timezone
# Create your models here.


class User(AbstractUser):
    special_user = models.DateTimeField(default=timezone.now,verbose_name='تایم کاربر ویژه')
    is_verify = models.BooleanField(default=False)
    auth_token = models.CharField(max_length=100,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    image = models.ImageField(upload_to='profileimages',null=True,blank=True)
    shortdes = models.TextField(null=True,blank=True)
    content = models.TextField(null=True,blank=True)
    slug = models.SlugField(default=uuid.uuid1, unique=True, allow_unicode=True, null=True, blank=True)
    rate = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.rate = self.rate_func()
        super().save(*args, **kwargs)


    def Is_special_user(self):
        if self.special_user > timezone.now():
            return True
        else:
            return False
    Is_special_user.boolean = True
    Is_special_user.short_description = 'وضعیت کاربر ویژه'


    def rate_func(self):
        try:
            a = self.blogauthor.all()
            b = 0
            for aa in a:
                b += aa.likes.count() - aa.dislike.count()
            return b
        except:
            pass
    def ratefind(self):
        aa =User.objects.all().order_by('-rate')
        b = 0
        for a in aa:
            if a.username == self.username:
                return b + 1
            else:
                b +=1