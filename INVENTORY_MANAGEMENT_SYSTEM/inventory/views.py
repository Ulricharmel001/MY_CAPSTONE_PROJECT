from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from .models import Store, Category

# ----------------------
# Django Form for Store
# ----------------------
class StoreForm(forms.ModelForm):
    """Form to create or edit a Store"""
    class Meta:
        model = Store
        fields = ['name', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Store Name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
        }

# ----------------------
# List all stores and add a new store
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
# Django Form for Category
# ----------------------
class CategoryForm(forms.ModelForm):
    """Form to create or edit a Category"""
    class Meta:
        model = Category
        fields = ['name', 'store']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'}),
            'store': forms.Select(attrs={'class': 'form-select'}),
        }

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



    # ----------------------
# Delete a store
# ----------------------
def store_delete(request, pk):
    """Delete a store and redirect to store list"""
    store = get_object_or_404(Store, pk=pk)
    if request.method == 'POST':
        store.delete()
        return redirect('store-list')
    return render(request, 'inventory/store_confirm_delete.html', {'store': store})


# ----------------------
# Delete a category
# ----------------------
def category_delete(request, pk):
    """Delete a category and redirect to category list"""
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'inventory/category_confirm_delete.html', {'category': category})

