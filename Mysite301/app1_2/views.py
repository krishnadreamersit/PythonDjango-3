from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # Receive value form url
    tmpid = request.GET.get('id')
    tmpname = request.GET.get('name')

    # Sending value to html template
    context = {'id': tmpid, 'name': tmpname} # Packaging received value
    return render(request, 'app1_2/index.html', context)


def get_value2(request, pid):
    context = {'pid': pid}
    return render(request, 'app1_2/display2.html', context)


def display_links(request):
    # str1 = "<p><a href='../getvalues1?id=1&name=Bikki'>Send Value1</a></p>"
    # str1 += "<p><a href='../getvalues2/1'>Send Value2</a></p>"
    # return HttpResponse(str1)
    return render(request, 'app1_2/links.html')


def display_form(request):
    return render(request, 'app1_2/form1.html')


def get_values3(request):
    # get values from url
    pid = request.GET.get('txt_id')
    fullname = request.GET.get('txt_name')
    address = request.GET.get('txt_address')
    context = {'pid': pid, 'fullname':fullname, 'address': address}
    return render(request, 'app1_2/display3.html', context)

def get_values4(request):
    # get values from url
    pid = request.POST.get('txt_id')
    fullname = request.POST.get('txt_name')
    address = request.POST.get('txt_address')
    context = {'pid': pid, 'fullname':fullname, 'address': address}
    return render(request, 'app1_2/display3.html', context)


def get_values5(request):
    if(request.method=='GET'):
        # display form
        return render(request, 'app1_2/form2.html')
    elif(request.method=='POST'):
        # receive values from url
        # get values from url
        pid = request.POST.get('txt_id')
        fullname = request.POST.get('txt_name')
        address = request.POST.get('txt_address')
        context = {'pid': pid, 'fullname':fullname, 'address': address}
        return render(request, 'app1_2/display3.html', context)