from django.urls import path
from . import views

urlpatterns = [
    path('like/<slug>', views.postlike, name='bloglike'),
    path('dislike/<slug>', views.postdislike, name='blogdislike'),
    path('finishbook/<id>', views.finishbook, name='finishbook'),
    path('deletbookfromlist/<id>', views.deletbook, name='deletbookfromlist'),
    path('add', views.addblog, name='addblog'),
    path('show/<slug>', views.blogshow, name='blogshow'),
    path('detail/<slug>', views.blogsdetail, name='blogsdetail'),




]



