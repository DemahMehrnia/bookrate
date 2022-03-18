from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home_Page, name='home_page'),
    path('writer', views.authorshow, name='authorshow'),
    path('writer/detail/<slug>', views.authorshowdetail, name='authorshowdetail'),
    path('topusers/', views.topusers, name='topusers'),


]


