from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from .models import PurchaseOrder, SalesOrder
from .forms import PurchaseOrderForm, SalesOrderForm

# ----------------------
# List all purchases
# ----------------------
class PurchaseOrderListView(LoginRequiredMixin, ListView):
    model = PurchaseOrder
    template_name = 'stock/purchase_list.html'
    context_object_name = 'purchases'
    ordering = ['-date']  # latest first

# ----------------------
# Create a new purchase
# ----------------------
class PurchaseOrderCreateView(LoginRequiredMixin, CreateView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm
    template_name = 'stock/purchase_form.html'
    success_url = reverse_lazy('purchase_list')

# ----------------------
# List all sales
# ----------------------
class SalesOrderListView(LoginRequiredMixin, ListView):
    model = SalesOrder
    template_name = 'stock/sale_list.html'
    context_object_name = 'sales'
    ordering = ['-date']  # latest first

# ----------------------
# Create a new sale
# ----------------------
class SalesOrderCreateView(LoginRequiredMixin, CreateView):
    model = SalesOrder
    form_class = SalesOrderForm
    template_name = 'stock/sale_form.html'
    success_url = reverse_lazy('sale_list')
