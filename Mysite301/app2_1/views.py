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
    # return render(request, 'app2_1/new.html', context)

    # Search Record
    # person = Person.objects.get(pid=10)
    # print(person)

    # Filter Records
    # persons = Person.objects.filter() # All Records
    # return render(request, 'app2_1/new.html', {'persons':persons})

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

"""
def crud(request):
# Save Record
    # person1 = Person(pid=1, full_name="Raj Rai", contact_address="Kthmandu")
    # person1.save()

    # person2 = Person()
    # person2.pid=2
    # person2.full_name="Kiran Rai"
    # person2.contact_address="Lalitpur"
    # person2.save()

    # clien1 = Client(full_name='Rhydam', contact_address='Kathmandu')
    # clien1.save()

    # clien2 = Client()
    # clien2.full_name="Rima"
    # clien2.contact_address = "Lalitpur"
    # clien2.save()
    # print(clien2.id)

    # person1 = Person(pid=1, full_name="Raj Rai", contact_address="Kthmandu")
    # person1.save()

    # person2 = Person()
    # person2.pid=2
    # person2.full_name="Kiran Rai"
    # person2.contact_address="Lalitpur"
    # person2.save()

    # person3 = Person.objects.create(pid=3, full_name='Reema Thapa',contact_address='Bhaktapur')

# Select or Filter Records
    # Select All
    # all_clients = Client.objects.all()
    #for client in all_clients:
        #print(client)

    # Get Value
    # client = Client.objects.get(pk=1)
    # print("PK :", client)

    # Filter
    # result = Client.objects.filter(id=1)
    # result = Client.objects.filter(id=175)
    # result = Client.objects.filter(full_name='UTSAV')
    # result = Client.objects.filter(full_name__exact='UTSAV')
    # result = Client.objects.filter(full_name__contains='UTSAV')
    # result = Client.objects.filter(id=231, full_name__contains='UTSAV')
    # result = Client.objects.filter(contact_address__contains='DOL').filter(full_name__contains='UT')
    # result = Client.objects.all().exclude(id = 20)

    # result = Client.objects.exclude(contact_address='GORKHS')
    # result = Client.objects.exclude(id__gt=50)
    # result = Client.objects.filter(id__gt=50)
    # result = Client.objects.filter(contact_address='GORKHA')
    # result = Client.objects.filter(id__in=[2, 3])
    # result = Client.objects.filter(full_name__endswith='A')
    result = Client.objects.filter(full_name__startswith='A')

    for item in result:
        print(item)

    # Order By
    # result = Client.objects.all().order_by('id')
    # result = Client.objects.all().order_by('-id')
    # result = Client.objects.order_by('-id').order_by('full_name').order_by('contact_address')

    # Result to Dict
    # results = Client.objects.values()
    # print(type(results))
    # print(type(results[0]))
    #return render(request, "app2_2/new.html", {'results':results})

    # Result to List
    # results = Client.objects.all()
    # print(type(results))
    # print(type(results[0]))
    # client = results[0]
    # print(type(client))
    # print(client.id, client.full_name, client.contact_address)
    # return render(request, "app2_2/new.html", {'results':results})

# Update
    # Individual Object Update
    # client = Client.objects.get(id=1)
    # client.full_name="RAJ"
    # client.contact_address="POKHARA"
    # client.save()

    # client = Client.objects.get(id=1)
    # client.full_name = "RAJ"
    # client.save()

    # client = Client.objects.get(id=1)
    # client.contact_address = "POKHARA"
    # client.save()

    # Bulk Update
    # Client.objects.select_for_update().filter(contact_address__contains='GOR').update(contact_address='PATAN')

# Delete
    # Individual Delete
    # client = Client.objects.get(id = 1)
    # client.delete()

    # Bulk Delete
    # Client.objects.select_for_update().filter(contact_address__contains='GOR').delete()
    return HttpResponse("Hello from Model CRUD")
"""