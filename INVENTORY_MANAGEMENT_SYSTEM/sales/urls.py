from django.urls import path
from .views import (
    SalesOrderListCreateView, SalesOrderDetailView,
    SalesItemListCreateView, SalesItemDetailView
)

urlpatterns = [
    # ----------------------
    # Sales Orders
    # ----------------------
    path('orders/', SalesOrderListCreateView.as_view(), name='sales-order-list'),
    path('orders/<int:pk>/', SalesOrderDetailView.as_view(), name='sales-order-detail'),

    # ----------------------
    # Sales Items
    # ----------------------
    path('items/', SalesItemListCreateView.as_view(), name='sales-item-list'),
    path('items/<int:pk>/', SalesItemDetailView.as_view(), name='sales-item-detail'),
]
