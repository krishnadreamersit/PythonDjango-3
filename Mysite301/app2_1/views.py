from django.shortcuts import render
from app2_1.models import Person

# Create your views here.

def index(request):
    # CRUD Operations using Model - in Code

    # Save Record-1
    # person1 = Person() # declare and initialize an object
    # person1.pid=5 # value set
    # person1.fullname = "Kiran Thapa"  # Value set
    # person1.contactaddress="BHK" # value set
    # person1.save() # Save

    # Save Record-2
    # person2 = Person(pid=6, fullname="Raj Rai", contactaddress="KTM")  # declare and initialize an object
    # person2.save()

    # Select All Records
    # persons = Person.objects.all() # All Records
    # print(len(persons)) # 6
    # for person in persons:
    #     print(person)
    # context = {'persons':persons}
    # return render(request, 'app2_1/index.html', context)

    # Search Record
    # person = Person.objects.get(pid=10)
    # print(person)

    # Filter Records
    # persons = Person.objects.filter() # All Records
    # return render(request, 'app2_1/index.html', {'persons':persons})

    # Update/Edit Record
    # person = Person.objects.get(pid=1)
    # print(person)
    # person.fullname="Kishor Sharma"
    # person.contactaddress = "Kalanki"
    # person.save()

    # Delete Record
    # person = Person.objects.get(pid=6)
    # person.delete()
    return render(request, 'app2_1/index.html')