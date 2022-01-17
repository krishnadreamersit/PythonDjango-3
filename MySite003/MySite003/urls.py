"""MySite003 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views # Step-1

urlpatterns = [
    # Step-2
    path('', views.home), # 127.0.0.1/home/ -> url pattern views.home -> function to call
    path('success/', views.successgallery),
    path('testimonials/', views.testimonials),
    path('admission/', views.onlineadmission),
    path('payment/', views.paymentoption),
    path('offers/', views.offers),
    path('career/', views.career),
    path('contactus/', views.contactus),
    path('blog/', views.blog),
    path('admin/', admin.site.urls), # System Defined
]
