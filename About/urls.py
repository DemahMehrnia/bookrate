from  django.urls import  path
from . import views

urlpatterns = [
    path('Me',views.About_page,name='about_page'),
    path('Booka',views.About_Booka,name='aboutbooka'),
    path('Bookazerotohundrd', views.bookazerotohundred, name='bookaztoh'),
    path('help', views.help, name='help'),
]