from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def video(request):
    return HttpResponse('<h1>By using zoom we can do video calling</h1>')

def message(reques):
    return HttpResponse('<h1>By using zoom we can do chatting</h1> ')
