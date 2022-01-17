# Step-1 - Import Library
from django.http import HttpResponse # return string as html
from django.shortcuts import render # return html file as html

# Step-2 - create new function
def home(request):
    str1 = "<html><head><style>body{padding-top:50pt;}</style><title>Welcome to broadwayinfosys.com</title></head><body bgcolor='blue' text='white'>"
    str1 = str1 + "<h1>Building Global IT Professionals since 2008</h1>"
    str1 = str1 +"<h3>AN ISO 9001:2015 CERTIFIED IT LEARNING CENTER</h3>"
    str1 = str1 +"<p>Broadway Infosys Nepal is one of the best inclusive computer training institutes in Kathmandu, Nepal. Established in 2008, our professional IT Training and Development center has been employing experts in this field to impart professional education.</p>"
    str1 = str1 +"</body></html>"
    return HttpResponse(str1)


def successgallery(request):
    return render(request, 'successgallery.html')
    # return HttpResponse("Success Galleries")

def testimonials(request):
    return render(request, 'testimonials.html')
    # return HttpResponse("Tentimonials")

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

