from django.shortcuts import render
from app3_1.forms import PersonForm
from app3_1.models import Person

# Create your views here.

def index(request):
    pform1 = PersonForm()
    if request.method=='POST':
        # Accept value from form
        pid = request.POST.get('pid')
        name = request.POST.get('fullname')
        address = request.POST.get('contactaddress')
        # print(pid, name, address)
        person1 = Person(pid=pid, name=name, address=address)
        person1.save()
        return render(request, 'app3_1/index.html', {'form1': pform1})
    else:
        # Display Web form
        return render(request, 'app3_1/index.html', {'form1':pform1})
