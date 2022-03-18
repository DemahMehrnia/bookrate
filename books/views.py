from django.shortcuts import render,redirect
from django.http import HttpResponse
from main_moudles.models import bookcategory,Books,bookwriter
from django.db.models import Q
from contact_us.forms import comenttous
from contact_us.models import coments
# Create your views here.
def bookshowdetail(request,slug):
    if request.method == 'POST':
        getedform = comenttous(request.POST)
        if getedform.is_valid():
            try:
                book = Books.objects.get(slug=slug)
                content = coments(
                    content=getedform.cleaned_data.get('text'),
                    comentuser=request.user,
                    forbook=book
                )
                content.save()
                return redirect('bookdetail' ,slug)
            except:
                return render(request,'account/eror.html')

    else:
        try:
            cat = bookcategory.objects.all()
            book = Books.objects.get(slug=slug)
            comentss = book.bookcoments.all()
            getcat = book.category.all().first()
            cats = bookcategory.objects.get(title=getcat)
            forshowbook = cats.bookcat.filter(~Q(slug=slug))[:3]
            comentform = comenttous()
            return render(request, 'books/booksdetail.html',
                          {'book': book, 'bookcategory': cat, 'books': forshowbook,'comentform':comentform,'coments':comentss})
        except:
            return render(request, 'account/eror.html')





def bookhomeshow(request,slug):
    try:
        cat = bookcategory.objects.all()
        showcat = bookcategory.objects.get(slug=slug)
        book = showcat.bookcat.all()
        return render(request, 'books/bookshow.html', {'bookcategory': cat,
        'books': book })
    except:
        cat = bookcategory.objects.all()
        books = Books.objects.all()
        return render(request, 'books/bookshow.html',{'bookcategory':cat,
        'books': books})

def booksfilter(request):
    pass


def booklike(request,slug):
    try:
        ourbook = Books.objects.get(slug=slug)
        user = request.user
        ourbook.likes.add(user)
        ourbook.dislike.remove(user)
        ourbook.save()
    except:
        ourbook.save()
    return redirect('bookdetail', ourbook.slug)

def bookdislike(request,slug):
    try:
        book = Books.objects.get(slug=slug)
        user = request.user
        book.dislike.add(user)
        book.likes.remove(user)
        book.save()
    except:
        book.save()
    return redirect('bookdetail', book.slug)

def bookreade(request,slug):
    try:
        ourbook = Books.objects.get(slug=slug)
        user = request.user
        ourbook.readed.add(user)
        ourbook.reading.remove(user)
        ourbook.save()
    except:
        ourbook.save()
    return redirect('bookdetail', ourbook.slug)

def bookreading(request,slug):
    try:
        ourbook = Books.objects.get(slug=slug)
        user = request.user
        ourbook.reading.add(user)
        ourbook.readed.remove(user)
        ourbook.save()
    except:
        ourbook.save()
    return redirect('bookdetail', ourbook.slug)
