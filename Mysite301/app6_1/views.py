from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # values - source (static, url, web form, file, database, network, api)
    id=1
    name="Bikki Goit"
    address ="KTM"
    office = "Broadway InfoSys"
    context = {'id':id, 'name':name, 'address':address, 'office': office}
    return render(request, 'app6_1/index.html', context)
