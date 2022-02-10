from django.shortcuts import render
from django.http import HttpResponseRedirect
from app4_1.forms import PersonForm

# Create your views here.

def index(request):
    form1 = PersonForm()
    if (request.method == 'POST'):
        form1 = PersonForm(request.POST)
        if form1.is_valid():
            form1.save()
        return HttpResponseRedirect('./index')
    else:
        return render(request, 'app4_1/index.html', {'form1': form1})




