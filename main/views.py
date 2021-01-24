from django.shortcuts import render, HttpResponse, redirect
from .models import Настройка 

# Create your views here.
def homepage(reguest):
    return render(reguest, 'index.html')

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
    return render(request, 'books.html', {"books": bib_books})