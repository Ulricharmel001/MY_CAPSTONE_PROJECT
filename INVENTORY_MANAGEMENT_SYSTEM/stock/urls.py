from django.urls import path
from . import views

urlpatterns = [
    path('purchases/', views.purchase_list, name='purchase_list'),# list of purchases
    path('sales/', views.sale_list, name='sale_list'),#list of sales transactions
    path('purchases/create/', views.create_purchase, name='create_purchase'),#purchase creation form
    path('sales/create/', views.create_sale, name='create_sale'), #sales  creation form
]
