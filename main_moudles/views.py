from django.db.models import Q
from django.shortcuts import render
# Create your views here.
from account.models import User
from blogs.models import blogs
from main_moudles.models import bookwriter, bookcategory, Books
from django.http import HttpResponse


def Home_Page(request):
    forshowbooks = Books.objects.all().order_by("-rate")[:3]
    forshowblogs = blogs.objects.all().order_by("-rate")[:4]
    newestblogs = blogs.objects.all().order_by("-created_at")[:4]
    return render(request, 'main_moudles/mainlist.html',{'books':forshowbooks,'blogs':forshowblogs,'blogg':newestblogs})

def site_header_component(request):
    return render(request, 'shared/site_header_Partial.html')

def site_footer_component(request):
    return render(request, 'shared/site_footer_Partial.html')

def authorshow(request):
    writers = bookwriter.objects.all()
    cat = bookcategory.objects.all()
    books = Books.objects.all()
    return render(request, 'main_moudles/authorshow.html', {'writers': writers,'bookcategory':cat,
        'books': books})

def authorshowdetail(request,slug):
    try:
        cat = bookcategory.objects.all()
        author = bookwriter.objects.get(slug=slug)
        cats = Books.objects.filter(author=author.id)[:3]
        return render(request, 'main_moudles/authordetail.html',{'writer': author, 'bookcategory': cat,'forshowbooks':cats})
    except:
        return render(request, 'account/eror.html')


def topusers(request):
    a= User.objects.all().order_by('-rate')[:10]
    return render(request,'main_moudles/top.html',{'tops':a,'num': 1})