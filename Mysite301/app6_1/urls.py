from django.urls import path
from . import views # 1

urlpatterns = [
    path('', views.index),
    path('filters', views.filter_test),
]