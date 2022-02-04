from django.shortcuts import render

# Create your views here.


def index(request):
    # CRUD Operations using Model - in Code
    return render(request, 'app2_1/index.html')