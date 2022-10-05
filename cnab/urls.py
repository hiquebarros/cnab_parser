from django.urls import path
from . import views

urlpatterns = [
    path('cnab/', views.upload_file),
    path('cnab/<store_name>/', views.get_operations)
]