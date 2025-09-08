from django.urls import path
from .views import (
    PurchaseOrderListView, PurchaseOrderCreateView,
    SalesOrderListView, SalesOrderCreateView
)

urlpatterns = [
    # Purchases
    path('purchases/', PurchaseOrderListView.as_view(), name='purchase_list'),
    path('purchases/create/', PurchaseOrderCreateView.as_view(), name='create_purchase'),

    # Sales
    path('sales/', SalesOrderListView.as_view(), name='sale_list'),
    path('sales/create/', SalesOrderCreateView.as_view(), name='create_sale'),
]
