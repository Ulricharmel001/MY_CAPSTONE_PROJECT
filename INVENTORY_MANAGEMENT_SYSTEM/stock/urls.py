from django.urls import path
from . import views

urlpatterns = [
    path('purchase/create/', views.create_purchase, name='create_purchase'),
    path('sales/create/', views.create_sale, name='create_sale'),
    path('purchase/list/', views.purchase_list, name='purchase_list'),
    path('sales/list/', views.sale_list, name='sale_list'),
]
