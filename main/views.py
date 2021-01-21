from django.shortcuts import render,HttpResponse

# Create your views here.
def homepage(reguest):
    return render(reguest, 'index.html')

def go(reguest):
    return HttpResponse('This is my first page')

def third(reguest):
    return HttpResponse('This is page test3')