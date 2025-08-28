from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import PurchaseOrder, PurchaseItem
from .serializers import PurchaseOrderSerializer, PurchaseItemSerializer

# ----------------------
# PurchaseOrder Views
# ----------------------

# List all purchase orders or create a new one
class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all().order_by('-date')
    serializer_class = PurchaseOrderSerializer

# Retrieve, update, or delete a single purchase order
class PurchaseOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

# ----------------------
# PurchaseItem Views
# ----------------------

# List all purchase items or create a new one
class PurchaseItemListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseItem.objects.all()
    serializer_class = PurchaseItemSerializer

# Retrieve, update, or delete a single purchase item
class PurchaseItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseItem.objects.all()
    serializer_class = PurchaseItemSerializer



from django.shortcuts import render, redirect, get_object_or_404
from .models import PurchaseOrder, PurchaseItem
from .forms import PurchaseOrderForm, PurchaseItemForm

# List all purchase orders
def purchase_order_list(request):
    orders = PurchaseOrder.objects.prefetch_related("items__product", "supplier").all()
    return render(request, "purchase/order_list.html", {"orders": orders})

# Create purchase order
def purchase_order_create(request):
    if request.method == "POST":
        form = PurchaseOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect("purchase_order_add_items", pk=order.id)
    else:
        form = PurchaseOrderForm()
    return render(request, "purchase/order_form.html", {"form": form})

# Add items to purchase order
def purchase_order_add_items(request, pk):
    order = get_object_or_404(PurchaseOrder, pk=pk)
    if request.method == "POST":
        form = PurchaseItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.purchase_order = order
            item.save()
            return redirect("purchase_order_add_items", pk=order.id)
    else:
        form = PurchaseItemForm()
    items = order.items.all()
    return render(request, "purchase/order_items_form.html", {"form": form, "order": order, "items": items})

# Update purchase order
def purchase_order_update(request, pk):
    order = get_object_or_404(PurchaseOrder, pk=pk)
    if request.method == "POST":
        form = PurchaseOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("purchase_order_list")
    else:
        form = PurchaseOrderForm(instance=order)
    return render(request, "purchase/order_form.html", {"form": form})

# Delete purchase order
def purchase_order_delete(request, pk):
    order = get_object_or_404(PurchaseOrder, pk=pk)
    if request.method == "POST":
        order.delete()
        return redirect("purchase_order_list")
    return render(request, "purchase/order_confirm_delete.html", {"order": order})

