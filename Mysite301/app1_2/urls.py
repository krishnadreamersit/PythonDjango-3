from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), #http://127.0.0.1:8000?id=1&name=Sanjaya
    path('getvalues2/<pid>', views.get_value2), #http://127.0.0.1:8000/app1_2/getvalues2/1
]
