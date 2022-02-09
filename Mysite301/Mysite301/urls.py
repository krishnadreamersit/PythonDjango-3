"""Mysite301 URL Configuration

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
from django.urls import path, include

urlpatterns = [
    path('app1_1/', include('app1_1.urls')), #http://127.0.0.1:8000/app1_1/
    path('app1_2/', include('app1_2.urls')), #http://127.0.0.1:8000/app1_2/
    path('app1_3/', include('app1_3.urls')), #http://127.0.0.1:8000/app1_3/
    path('app1_4/', include('app1_4.urls')), # http://127.0.0.1:8000/app1_4/

    path('app2_1/', include('app2_1.urls')),
    path('app3_1/', include('app3_1.urls')),
    path('admin/', admin.site.urls),
]