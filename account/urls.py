from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagelogin, name='mainloginpage'),
    path('Logein', views.llogin, name='loginpage'),
    path('Signin', views.signup, name='signinpage'),
    path('verify/<ourtoken>', views.verify, name="verify"),
    path('home/', views.home, name='home',),
    path('home/detail/<slug>', views.detailshow, name='homedetailshow',),
    #path('ba/', views.test, name='cygchome',),

]



