from django.urls import path
from . import views # 1

urlpatterns = [
    path('', views.index, name='home'), # Display all
    path('display_new', views.display_new, name="display_new"), # Display New Form
    path('insert/', views.insert), # Save Record
    path('display_edit', views.display_edit, name="edit"), # Display Edit Form
    path('update/', views.update), # Update Record
    path('display_delete', views.display_delete, name="display_delete"), # Display Delete Form
    path('display_delete_confirm', views.display_delete_confirm), # Confirm Delete form
    path('delete/', views.delete), # Delete Record
]