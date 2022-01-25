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