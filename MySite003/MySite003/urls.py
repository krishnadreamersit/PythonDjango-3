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

# Step-1
from app1.views import index, hello
from app2 import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Step-2 create new url pattern
    path('app1/', index),
    path('app12/', hello),
    path('app2/', v2.index),
    path('app2_1/', v2.load_html),

    path('app2/about', v2.about),
    path('app2/contact', v2.contact),
    path('app2/index', v2.index),
    path('app2/services', v2.services),
]
