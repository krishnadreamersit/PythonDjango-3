from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello from app2")

def load_html(request):
    return render(request, 'app2/index.html')

def about(request):
    return render(request, 'app2/about.html')

def contact(request):
    return render(request, 'app2/contact.html')

def index(request):
    return render(request, 'app2/index1.html')

def services(request):
    return render(request, 'app2/services.html')