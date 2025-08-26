from django.urls import path
from .views import (
    PurchaseOrderListCreateView, PurchaseOrderDetailView,
    PurchaseItemListCreateView, PurchaseItemDetailView
)

urlpatterns = [
    # Purchase Orders
    path('orders/', PurchaseOrderListCreateView.as_view(), name='purchase-order-list'),
    path('orders/<int:pk>/', PurchaseOrderDetailView.as_view(), name='purchase-order-detail'),

    # Purchase Items
    path('items/', PurchaseItemListCreateView.as_view(), name='purchase-item-list'),
    path('items/<int:pk>/', PurchaseItemDetailView.as_view(), name='purchase-item-detail'),
]
