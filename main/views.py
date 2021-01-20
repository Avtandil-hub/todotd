from django.shortcuts import render,HttpResponse

# Create your views here.
def homepage(reguest):
    return HttpResponse('Hello')

def go(reguest):
    return HttpResponse('This is my first page')
