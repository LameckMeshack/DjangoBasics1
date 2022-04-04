from django.http import HttpResponse
from django.shortcuts import render

# request -> response
def say_Hello(request):
    return render(request, 'hello.html',{"name":"Lameck"})
