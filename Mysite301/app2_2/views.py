from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Person
from .models import Student
from .models import Client


# Create your views here.
def index(request):
    persons = Person.objects.all()
    return render(request, 'app2_2/index.html', {'persons': persons})


def display_new(request):
    return render(request, 'app2_2/add_new.html')


def insert(request):
    if request.method == 'GET':
        person = Person()
        person.pid = request.GET.get('txt_id')
        person.full_name = request.GET.get('txt_name')
        person.contact_address = request.GET.get('txt_address')
        person.save()
    else:
        person = Person()
        person.pid = request.POST.get('txt_id')
        person.full_name = request.POST.get('txt_name')
        person.contact_address = request.POST.get('txt_address')
        person.save()
    return HttpResponseRedirect("..")


def display_edit(request):
    pid = request.GET.get('pid')
    person = Person.objects.get(pid=pid)
    print("For Edit ", person)
    return render(request, 'app2_2/edit.html', {'person': person})

def update(request):
    pid = request.POST.get('txt_id')
    person = Person.objects.get(pid=pid)
    person.full_name = request.POST.get('txt_name')
    person.contact_address = request.POST.get('txt_address')
    person.save()
    return HttpResponseRedirect("..")

def display_delete(request):
    pid = request.GET.get('pid')
    person = Person.objects.get(pid=pid)
    return render(request, 'app2_2/delete.html', {'person': person})


def display_delete_confirm(request):
    pid = request.POST.get('txt_id')
    print("pid -> ", pid)
    return render(request, 'app2_2/display_confirmation.html', {'pid': pid})


def delete(request):
    pid = request.POST.get('txt_id')
    person = Person.objects.get(pid=pid)
    person.delete()
    return HttpResponseRedirect("..")
