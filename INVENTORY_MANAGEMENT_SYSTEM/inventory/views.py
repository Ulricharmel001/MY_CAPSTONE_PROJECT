from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, DeleteView
from .models import Store, Category, Product, Customer, Supplier
from .forms import StoreForm, CategoryForm, ProductForm, CustomerForm, SupplierForm

# ----------------------
# Reusable List + Create Mixin
# ----------------------
class ListCreateMixin(LoginRequiredMixin, ListView):
    """
    Handles displaying a list of objects and creating a new object via POST.
    """
    form_class = None  # Must be defined in subclass
    success_url = None

    def get_queryset(self):
        # Only objects owned by the current user
        return self.model.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect(self.success_url)
        self.object_list = self.get_queryset()
        context = self.get_context_data(form=form)
        return self.render_to_response(context)


# ----------------------
# Store Views
# ----------------------
class StoreListView(ListCreateMixin):
    model = Store
    form_class = StoreForm
    template_name = 'inventory/store_list.html'
    context_object_name = 'stores'
    success_url = reverse_lazy('store-list')


class StoreDetailView(LoginRequiredMixin, UpdateView):
    model = Store
    form_class = StoreForm
    template_name = 'inventory/store_detail.html'
    success_url = reverse_lazy('store-list')

    def get_queryset(self):
        return Store.objects.filter(user=self.request.user)


class StoreDeleteView(LoginRequiredMixin, DeleteView):
    model = Store
    template_name = 'inventory/store_confirm_delete.html'
    success_url = reverse_lazy('store-list')

    def get_queryset(self):
        return Store.objects.filter(user=self.request.user)


# ----------------------
# Category Views
# ----------------------
class CategoryListView(ListCreateMixin):
    model = Category
    form_class = CategoryForm
    template_name = 'inventory/category_list.html'
    context_object_name = 'categories'
    success_url = reverse_lazy('category-list')


class CategoryDetailView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'inventory/category_detail.html'
    success_url = reverse_lazy('category-list')

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'inventory/category_confirm_delete.html'
    success_url = reverse_lazy('category-list')

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


# ----------------------
# Product Views
# ----------------------
class ProductListView(ListCreateMixin):
    model = Product
    form_class = ProductForm
    template_name = 'inventory/product_list.html'
    context_object_name = 'products'
    success_url = reverse_lazy('product-list')


class ProductDetailView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "inventory/product_detail.html"
    success_url = reverse_lazy("product-list")

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "inventory/product_confirm_delete.html"
    success_url = reverse_lazy("product-list")

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)


# ----------------------
# Customer Views
# ----------------------
class CustomerListView(ListCreateMixin):
    model = Customer
    form_class = CustomerForm
    template_name = 'inventory/customer_list.html'
    context_object_name = 'customers'
    success_url = reverse_lazy('customer-list')


class CustomerDetailView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'inventory/customer_detail.html'
    success_url = reverse_lazy('customer-list')

    def get_queryset(self):
        return Customer.objects.filter(user=self.request.user)


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = 'inventory/customer_confirm_delete.html'
    success_url = reverse_lazy('customer-list')

    def get_queryset(self):
        return Customer.objects.filter(user=self.request.user)
    




# ----------------------
# Supplier Views
# ----------------------
class SupplierListView(ListCreateMixin):
    model = Supplier
    form_class = SupplierForm
    template_name = 'inventory/supplier_list.html'
    context_object_name = 'suppliers'
    success_url = reverse_lazy('supplier-list')


class SupplierDetailView(LoginRequiredMixin, UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'inventory/supplier_detail.html'
    success_url = reverse_lazy('supplier-list')

    def get_queryset(self):
        return Supplier.objects.filter(user=self.request.user)


class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = Supplier
    template_name = 'inventory/supplier_confirm_delete.html'
    success_url = reverse_lazy('supplier-list')

    def get_queryset(self):
        return Supplier.objects.filter(user=self.request.user)
