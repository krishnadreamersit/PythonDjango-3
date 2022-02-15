from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index), # display all
    path('new', views.new_form), # display entry form
    path('save', views.save), # save record
    path('edit', views.edit), # display edit form
    path('update', views.upate), # update record
    path('delete', views.delete), # delete record
]