from django.shortcuts import render,HttpResponse
from .models import TODO

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

def test(reguest):
    TODO_list = TODO.objects.all()
    return render(reguest,'test.html')