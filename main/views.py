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
    subtitle = form['book_subtitle']
    description = form['book_description']
    price = form['book_price']
    genre = form['book_genre']
    author = form['book_author']
    year = form['book_year']
    book = books(title=title, subtitle=subtitle, description=description, price=price, genre=genre, author=author, year=year)
    book.save()
    return redirect(bookss)

def delete_todo(reguest, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(homepage)

def delete_book(reguest, id):
    book = books.objects.get(id=id)
    book.delete()
    return redirect(bookss)

def mark_book(reguest, id):
    book = books.objects.get(id=id)
    book.is_favorite = False
    book.save()
    return redirect(bookss)

def marked_book(reguest, id):
    book = books.objects.get(id=id)
    book.is_favorite = True
    book.save()
    return redirect(bookss)
