from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index),
    path('new', views.new_form),
    path('save', views.save),
]