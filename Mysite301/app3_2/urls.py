from django.urls import path
from . import views # 1

urlpatterns = [
    path('show',views.show),
    path('new/', views.new),
    path('edit/<int:id>', views.edit),
    path('update', views.update),
    path('delete/<int:id>', views.destroy),
]