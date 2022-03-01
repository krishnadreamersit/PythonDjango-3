from django.urls import path
from .views import EmailAttachementView

urlpatterns = [
    path('', EmailAttachementView.as_view(), name='emailattachment')
]