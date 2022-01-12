# Step-1 - Import Library
from django.http import HttpResponse

# Step-2 - create new function
def home(request):
    return HttpResponse("Welcome to Broadway InfoSys Nepal")

def successgallery(request):
    return HttpResponse("Success Galleries")

def testimonials(rerquest):
    return HttpResponse("Tentimonials")

def onlineadmission(request):
    return HttpResponse("Online Admission")

def paymentoption(request):
    return HttpResponse("Payment Option")

def offers(request):
    return HttpResponse("Offers")

def career(request):
    return HttpResponse("Career")

def contactus(request):
    return HttpResponse("Contact Us")

def blog(request):
    return HttpResponse("Blog")

