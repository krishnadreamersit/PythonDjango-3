from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('getvalues1', views.index), #http://127.0.0.1:8000?id=1&name=Sanjaya
    path('getvalues2/<pid>', views.get_value2), #http://127.0.0.1:8000/app1_2/getvalues2/1
    path('displaylinks/', views.display_links), #http://127.0.0.1:8000/app1_2/displaylinks
    path('displayform', views.display_form), #http://127.0.0.1:8000/app1_2/displayform
    path('getvalues3', views.get_values3), #http://127.0.0.1:8000/app1_2/getvalues3
    path('getvalues4', views.get_values4), #http://127.0.0.1:8000/app1_2/getvalues4
    path('getvalues5', views.get_values5), #http://127.0.0.1:8000/app1_2/getvalues5
]