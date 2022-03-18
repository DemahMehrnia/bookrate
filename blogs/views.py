from django.shortcuts import render,redirect
from .models import blogs
from main_moudles.models import Books
from account.models import User
from .forms import add_blog
from contact_us.forms import blogcoment
from contact_us.models import coments as em
from django.db.models import Q
from django.http import HttpResponse


# Create your views here.
def postlike(request,slug):
    try:
        ourblog = blogs.objects.get(slug=slug)
        user = request.user
        ourblog.likes.add(user)
        ourblog.dislike.remove(user)
        ourblog.save()
        a = ourblog.author
        a.save()
    except:
        ourblog.save()
    return redirect('blogsdetail', ourblog.slug)

def postdislike(request,slug):
    try:
        blog = blogs.objects.get(slug=slug)
        user = request.user
        blog.dislike.add(user)
        blog.likes.remove(user)
        blog.save()
        a = blog.author
        a.save()
    except:
        blog.save()
    return redirect('blogsdetail', blog.slug)

def finishbook(request,id):
    try:
        book = Books.objects.get(id=id)
        user = request.user
        book.reading.remove(user)
        book.readed.add(user)
        return redirect('home')
    except:
        return render(request, 'account/eror.html')

def deletbook(request,id):
    try:
        book = Books.objects.get(id=id)
        user = request.user
        if user in book.reading.all():
            book.reading.remove(user)
            return redirect('home')
        elif user in book.readed.all():
            book.readed.remove(user)
            return redirect('home')
    except:
        return render(request, 'account/eror.html')

def blogshow(request,slug):
    if slug == 'newest':
        forshow = blogs.objects.all().order_by("-id")
        what = 'اخرین مقاله ها'
    else:
        forshow = blogs.objects.all().order_by("-rate")
        what = 'محبوب ترین  مقاله ها'
    return render(request,'blogs/blogshow.html',{'blogs':forshow,'what' : what})



def addblog(request):
    try:
        if request.user.is_verify:
            if request.method == 'POST':
                try:
                    data = request.POST
                    image = request.FILES.get('image')
                    content = blogs(
                        title=data['title'],
                        image=image,
                        short_description=data['shortdes'],
                        content=data['contet'],
                        author=request.user
                        )
                    content.save()
                    return render(request, 'contact_us/Succes.html')
                except:
                    return render(request,'account/eror.html')
            else:
                formblog = add_blog()
                return render(request,'blogs/addblog.html',{'form': formblog})
        else:
            return render(request, 'account/mainlogin.html', {'from': True})
    except:
        return render(request, 'account/mainlogin.html', {'from': True})

def blogsdetail(request,slug):
    try:
        if request.method == 'POST':
            getedform = blogcoment(request.POST)
            if getedform.is_valid():
                ourblog = blogs.objects.get(slug=slug)
                content = em(
                    content=getedform.cleaned_data.get('text'),
                    comentuser=request.user,
                    forblog= ourblog
                 )
                content.save()
                return redirect('blogsdetail', slug)
        else:
            getedform = blogcoment(request.POST)
            forshow = blogs.objects.get(slug=slug)
            test = forshow.author
            forshowblogs = blogs.objects.filter(~Q(title=forshow.title),Q(author=test))[:3]
            coments = forshow.blogcoments.all()

            return render(request,'blogs/blogsdetail.html',{'blog':forshow,'form':getedform,'coments':coments,'blogs':forshowblogs })
    except:
        return render(request,'account/eror.html')

