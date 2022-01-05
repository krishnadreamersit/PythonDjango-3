from django.shortcuts import render

# Step-1
from django.http import HttpResponse # generate output

# Create your views here.

# Step-2
def index(request):
    return HttpResponse("Hello from app1")


def hello(request):
    str1 = "<html>"
    str1 = str1 + "<head>"
    str1 = str1 + "<title>First Web Page</title>"
    str1 = str1 + "</head>"
    str1 = str1 + "<body>"
    str1 = str1 + "<h1>Hello from hello()</h1>"
    str1 = str1 + "</body>"
    str1 = str1+"</html>"
    return HttpResponse(str1)