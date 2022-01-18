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

from . import views as v1   # Step-1
from app1_1 import views as v2
from app1_2 import views as v3

urlpatterns = [
    # Step-2
    path('', v1.index), # 127.0.0.1/home/ -> url pattern views.home -> function to call
    path('success/', v1.successgallery),
    path('testimonials/', v1.testimonials),
    path('admission/', v1.onlineadmission),
    path('payment/', v1.paymentoption),
    path('offers/', v1.offers),
    path('career/', v1.career),
    path('contactus/', v1.contactus),
    path('blog/', v1.blog),
    path('index/', v2.index),
    path('index2/', v3.index),
    path('admin/', admin.site.urls), # System Defined
]
