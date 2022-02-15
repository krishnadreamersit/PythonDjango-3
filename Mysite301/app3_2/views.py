from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def show(request):
    employees = Employee.objects.all()
    print(employees)
    return render(request, "app3_2/index.html", {'employees':employees})


def new(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        contact_address = request.POST.get('contact_address')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        employee = Employee(full_name=full_name, contact_address=contact_address, mobile=mobile, email=email)
        employee.save()
        return HttpResponseRedirect('../show')
    else:
        form = EmployeeForm()
        return render(request, 'app3_2/new.html', {'form':form})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request,'app3_2/edit.html', {'employee':employee})


def update(request):
    if request.method=='POST':
        empid = request.POST.get('empid')
        full_name = request.POST.get('full_name')
        contact_address = request.POST.get('contact_address')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        employee = Employee(id=empid, full_name=full_name, contact_address=contact_address, mobile=mobile, email=email)
        employee.save()
        return HttpResponseRedirect('./show')
    return HttpResponseRedirect('./show')

def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return HttpResponseRedirect('../show')