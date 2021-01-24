from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo 
from .models import books

# Create your views here.
def homepage(reguest):
    todo = ToDo.objects.all()
    return render(reguest, 'index.html', {'todo': todo})

def go(reguest):
    return HttpResponse('This is my first page')

def third(reguest):
    return HttpResponse('This is page test3')

def add(reguest):
    return render(reguest, 'add.html')

def tap(reguest):
    return render(reguest, 'tap.html')

def apk(reguest):
    return render(reguest, 'apk.html')

def bookss(request):
    bib_books = books.objects.all()
    return render(request, 'books.html', {"bib_books": bib_books})

def add_book(reguest):
    form = reguest.POST
    title = form['book_text']
    book = books(title=title)
    book.save()
    return  redirect(bookss)
