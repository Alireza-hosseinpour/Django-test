from django.urls import path
from .views import index, list_of_products

app_name='products'

urlpatterns = [
    path('', index, name='index'),
    path('list_of_products/', list_of_products, name='list_of_products')
]
