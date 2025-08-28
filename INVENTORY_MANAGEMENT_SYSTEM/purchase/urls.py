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


from django.urls import path
from . import views

urlpatterns = [
    # Purchase Order CRUD
    path('', views.purchase_order_list, name='purchase_order_list'),
    path('create/', views.purchase_order_create, name='purchase_order_create'),
    path('<int:pk>/update/', views.purchase_order_update, name='purchase_order_update'),
    path('<int:pk>/delete/', views.purchase_order_delete, name='purchase_order_delete'),

    # Add items to purchase order
    path('<int:pk>/add-items/', views.purchase_order_add_items, name='purchase_order_add_items'),
]
