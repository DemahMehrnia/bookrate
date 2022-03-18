from django.db import models

# Create your models here.
from blogs.models import blogs
from main_moudles.models import Books


class ContactUs(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    full_name = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    message = models.TextField(verbose_name='متن تماس با ما')
    created_date = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    response = models.TextField(verbose_name='متن پاسخ تماس با ما', null=True, blank=True)
    is_read_by_admin = models.BooleanField(verbose_name='خوانده شده توسط ادمین',default=False)

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'

    def __str__(self):
        return self.title

class coments(models.Model):
    comentuser = models.CharField(max_length=50,null=True)
    content = models.TextField(verbose_name='متن کامنت')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    forbook = models.ForeignKey(Books, on_delete=models.CASCADE, null=True,related_name='bookcoments')
    forblog = models.ForeignKey(blogs, on_delete=models.CASCADE, null=True,related_name='blogcoments')


