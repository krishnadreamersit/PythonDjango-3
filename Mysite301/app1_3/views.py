from django.shortcuts import render
from app1_3.mydatabase import MyDatabase
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    # get all records from database
    # send all records to index.html file
    mydb = MyDatabase();
    persons = mydb.select_all2()
    # for person in persons:
    #     print(person)
    context = {'persons': persons}
    return render(request, 'app1_3/index.html', context)


def new_form(request):
    return render(request, 'app1_3/new.html')


def save(request):
    # Read values
    pid = request.POST.get('txtID')
    name = request.POST.get('txtName')
    address = request.POST.get('txtAddress')
    mydb = MyDatabase(); # Create database object
    result = mydb.insert_record(pid, name, address) # insert record in database
    return HttpResponseRedirect('index')

