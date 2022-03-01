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

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('app1_1/', include('app1_1.urls')), #http://127.0.0.1:8000/app1_1/
    path('app1_2/', include('app1_2.urls')), #http://127.0.0.1:8000/app1_2/
    path('app1_3/', include('app1_3.urls')), #http://127.0.0.1:8000/app1_3/
    path('app1_4/', include('app1_4.urls')), # http://127.0.0.1:8000/app1_4/
    path('app2_1/', include('app2_1.urls')),
    path('app2_2/', include('app2_2.urls')),
    path('app3_1/', include('app3_1.urls')),
    path('app3_2/', include('app3_2.urls')),
    path('app4_1/', include('app4_1.urls')),
    path('app4_2/', include('app4_2.urls')),
    path('app5_1/', include('app5_1.urls')),
    path('app6_1/', include('app6_1.urls')),
    path('app7_1/', include('app7_1.urls')), # User Management
    path('app8_1/', include('app8_1.urls')), # Session Management
    path('app8_2/', include('app8_2.urls')), # Cookie Management
    path('app9_1/', include('app9_1.urls')), # Non-HTML Content
    path('app10_1/', include('app10_1.urls')), # Sending Email
    path('app11_1/', include('app11_1.urls')), # Uploading File![](C:/Users/ASUS/AppData/Local/Temp/0-02-03-210a20fd4fb211362013daf9af35816ae098de897811d6e49ae31a4b65a63079_beef72025293ee64.jpg)
    path('app12_1/', include('app12_1.urls')), # Uploading File![](C:/Users/ASUS/AppData/Local/Temp/0-02-03-210a20fd4fb211362013daf9af35816ae098de897811d6e49ae31a4b65a63079_beef72025293ee64.jpg)
    path('app12_2/', include('app12_2.urls')),
    path('app12_2/', include('app12_2.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)