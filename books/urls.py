from django.urls import path
from . import views

urlpatterns = [
    path('detail/<slug>', views.bookshowdetail, name='bookdetail'),
    path('like/<slug>', views.booklike, name='booklike'),
    path('dislike/<slug>', views.bookdislike, name='bookdislike'),
    path('addtoreaded/<slug>', views.bookreade, name='bookreaded'),
    path('addtoreading/<slug>', views.bookreading, name='bookreading'),
    path('<slug>', views.bookhomeshow, name='bookshome'),

]


