from django.urls import path
from .views import product_materials

urlpatterns = [
    path('product_materials/', product_materials, name='product_materials'),
]