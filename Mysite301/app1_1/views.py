from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return  HttpResponse("Hello World of Django Site!") # return plain text

def about(request):
    str1 = "<h1>Title1</h1>"
    str1 = str1 + "<h2>Title2</h2>"
    str1 = str1 + "<p>Paragraph-1</p>"
    return HttpResponse(str1) # return HTML Text

def services(request):
    return render(request, 'app1_1/services.html')
