from django.urls import path
from . import views

urlpatterns = [
    path('purchases/', views.purchase_list, name='purchase_list'),
    path('sales/', views.sale_list, name='sale_list'),
    path('purchases/create/', views.create_purchase, name='create_purchase'),
    path('sales/create/', views.create_sale, name='create_sale'),
]
