from django.shortcuts import render
from .forms import sign_up_form,log_in_form
from .models import User
from django.shortcuts import redirect, render
from django.contrib import messages
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from blogs.models import blogs


# Create your views here.
from django.http import HttpResponse

def pagelogin(request):
    if request.method == 'POST':
       pass
    else:
        return render(request,'account/mainlogin.html')

def llogin(request):
    if request.method == 'POST':
        try:
            loginform = log_in_form(request.POST)
            if loginform.is_valid():
                username = request.POST.get('Logname')
                password = request.POST.get('Logpassword')
                ouruser = User.objects.filter(username=username).first()
                if ouruser is None:
                    messages.success(request, 'کاربر پیدا نشد')
                    return render(request, 'account/login.html')
                if not ouruser.is_verify:
                    messages.success(request, 'کاربر لینکی که به ایمیل فرستادیم را تایید نکرده')
                    return render(request, 'account/login.html')
                user = authenticate(username=username, password=password)
                if user is None:
                    messages.success(request, 'رمز عبور اشتباه است')
                    return render(request, 'account/login.html')
                login(request, user)
                return render(request, 'account/loggedin.html')
        except:
            return render(request,'account/eror.html')
    else:
        loginform = log_in_form()

    return render(request, 'account/login.html',{'loginn_form': loginform})


def signup(request):
    if request.method == 'POST':
        signupForm = sign_up_form(request.POST)
        if signupForm.is_valid():
            uusername = signupForm.cleaned_data.get('name_form')
            eemail = request.POST.get('email_form')
            ppassword = request.POST.get('password_form')
            try:
                if User.objects.filter(username=uusername).first():
                    messages.success(request, 'این نام قبلا انتخاب شده است')
                    return redirect('signinpage')

                if User.objects.filter(email=eemail).first():
                    messages.success(request, 'این ایمیل قبلا انتخاب شده است.')
                    return redirect('signinpage')
                our_token = str(uuid.uuid4())
                our_user = User(username=uusername, email=eemail, auth_token=our_token)
                our_user.set_password(ppassword)
                our_user.save()
                send_mail_after_registration(eemail, our_token)
                return render(request,'account/emailsended.html')
            except:
                return render(request,'account/eror.html')


    else:
        signupForm = sign_up_form

    return render(request, 'account/signup.html', {'signup_form': signupForm})


def send_mail_after_registration(email , token):
    subject = 'لینک تایید ایمیل '
    message ='برای تایید ایمیل کلیک کنید' + f'://127.0.0.1:8000/UserLog/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

def verify(request,ourtoken):
    try:
        userinfo = User.objects.filter(auth_token=ourtoken).first()
        if userinfo.is_verify:
            return render(request, 'account/very.html')
        userinfo.is_verify = True
        userinfo.save()
        return render(request, 'account/verified.html')

    except:
        return render(request, 'account/eror.html')

def home(request):
    try:
        cominguser = request.user
        if cominguser.is_verify:
            ourblogs = blogs.objects.filter(author=cominguser)[:4]
            readedbookas = cominguser.booksreaded.all()[:4]
            readingbook = cominguser.booksreading.all()[:4]
            return render(request, 'account/home.html', {'blogs': ourblogs ,
             'readedbook': readedbookas,
              'readingbook': readingbook})
        else:
            return render(request, 'account/mainlogin.html', {'from': True})
    except:
        return render(request, 'account/mainlogin.html', {'from': True})

def detailshow(request,slug):
    try:
        cominguser = request.user
        if cominguser.is_verify:
            if slug == 'myblogs':
                ourblogs = blogs.objects.filter(author=cominguser)
                return render(request,'account/detailshow.html',{'forshow': ourblogs,'st':slug})
            elif slug == 'myreadingbooks':
                readingbook = cominguser.booksreading.all()
                return render(request,'account/detailshow.html',{'forshow': readingbook,'st':slug})
            elif slug == 'myreadedbook':
                readedbookas = cominguser.booksreaded.all()
                return render(request,'account/detailshow.html',{'forshow': readedbookas,'st':slug})
        else:
            return render(request,'account/eror.html')
    except:
        return render(request, 'account/mainlogin.html', {'from': True})
#def test(request):
   # return render(request,'account/test.html')
