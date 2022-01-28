from django.shortcuts import render
from app1_3.mydatabase import MyDatabase

# Create your views here.


def index(request):
    # get all records from database
    # send all records to index.html file
    mydb = MyDatabase();
    mydb.select_all()
    return render(request, 'app1_3/index.html')
