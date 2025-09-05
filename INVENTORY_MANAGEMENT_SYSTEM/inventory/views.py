from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from .models import Store, Category, Supplier, Customer, Product
from .forms import CustomerForm, SupplierForm, StoreForm,CategoryForm, ProductForm
from django.db.models import Count

# ----------------------
# List all stores and add a new store here
# ----------------------
def store_list(request):
    """
    Handles displaying all stores and adding a new store via form.
    GET: Render template with all stores and empty form.
    POST: Process form submission to create a new store.
    """
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()  # Save new store
            return redirect('store-list')  # Redirect to refresh page
    else:
        form = StoreForm()  # Empty form for GET request

    stores = Store.objects.all()  # Fetch all stores
    return render(request, 'inventory/store_list.html', {'stores': stores, 'form': form})

# ----------------------
# View, edit, or delete a single store
# ----------------------
def store_detail(request, pk):
    """
    Handles displaying and updating a single store.
    GET: Show store details with pre-filled form.
    POST: Update store using form submission.
    """
    store = get_object_or_404(Store, pk=pk)

    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()  # Update store
            return redirect('store-list')
    else:
        form = StoreForm(instance=store)  # Pre-filled form

    return render(request, 'inventory/store_detail.html', {'store': store, 'form': form})


# ----------------------
# List all categories and add a new category
# ----------------------
def category_list(request):
    """
    GET: Render template showing all categories and a form to add a new category.
    POST: Process form to create a new category.
    """
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()

    categories = Category.objects.all()
    return render(request, 'inventory/category_list.html', {'categories': categories, 'form': form})

# ----------------------
# View, edit, or delete a single category
# ----------------------
def category_detail(request, pk):
    """
    GET: Render template showing a single category with pre-filled form.
    POST: Update category with submitted form data.
    """
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'inventory/category_detail.html', {'category': category, 'form': form})




# Delete a category

def category_delete(request, pk):
    """Delete a category and redirect to category list"""
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'inventory/category_confirm_delete.html', {'category': category})  

# Delete a store

def store_delete(request, pk):
    """Delete a store and redirect to store list"""
    store = get_object_or_404(Store, pk=pk)
    if request.method == 'POST':
        store.delete()
        return redirect('store-list')
    return render(request, 'inventory/store_confirm_delete.html', {'store': store})





# ----------------------
# List all products + add new
# ----------------------
def product_list(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()
    products = Product.objects.select_related("category", "supplier").all()
    return render(request, "inventory/product_list.html", {"products": products, "form": form})

# ----------------------
# Update a product
# ----------------------
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm(instance=product)
    return render(request, "inventory/product_detail.html", {"product": product, "form": form})







# ----------------------
# Delete a product
# ----------------------
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect("product_list")
    return render(request, "inventory/product_confirm_delete.html", {"product": product})

# ----------------------
# Customer CRUD list all customers of a store 
# ----------------------
def customer_list(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer-list')
    else:
        form = CustomerForm()
    customers = Customer.objects.all()
    return render(request, 'inventory/customer_list.html', {'customers': customers, 'form': form})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer-list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'inventory/customer_detail.html', {'customer': customer, 'form': form})

def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer-list')
    return render(request, 'inventory/customer_confirm_delete.html', {'customer': customer})


# ----------------------
# Supplier CRUD List all supplier of store here
# ----------------------
def supplier_list(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier-list')
    else:
        form = SupplierForm()
    suppliers = Supplier.objects.all()
    return render(request, 'inventory/supplier_list.html', {'suppliers': suppliers, 'form': form})

def supplier_detail(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('supplier-list')
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'inventory/supplier_detail.html', {'supplier': supplier, 'form': form})

def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        supplier.delete()
        return redirect('supplier-list')
    return render(request, 'inventory/supplier_confirm_delete.html', {'supplier': supplier})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm(instance=product)
    return render(request, "inventory/product_detail.html", {"product": product, "form": form})









