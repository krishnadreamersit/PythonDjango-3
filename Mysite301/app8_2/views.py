from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'app8_2/index.html')


def create_cookie(request):
    # Create cookie
    response = HttpResponse("Create Cookie Successfully")
    var1 = "Hello from Cookie"
    response.set_cookie('ck1', var1, 20) # ck1 name, var1 value, 20 lifetime
    return response


def display_cookie(request):
    # Getting cookie
    ck1_value = request.COOKIES['ck1']
    return HttpResponse("CK1 = " + ck1_value)
