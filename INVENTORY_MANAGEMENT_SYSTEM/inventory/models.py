from django.db import models

# ----------------------
# Store: Multi-location support
# ----------------------
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# ----------------------
# Category: Product categorization
# ----------------------
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,          # When Store is deleted → delete all Categories
        related_name='categories'
    )

    class Meta:
        unique_together = ('name', 'store')   # Prevent same category name in same store
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.store.name})"


# ----------------------
# Supplier: Provides products
# ----------------------
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True, unique=True)
    phone = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


# ----------------------
# Customer: End-user or client
# ----------------------
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True, unique=True)
    phone = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


# ----------------------
# Product: Inventory items
# ----------------------
class Product(models.Model):
    sku = models.CharField(max_length=50, unique=True) # sku stand for stock keeping unit
    name = models.CharField(max_length=100)
  
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,          # When Category is deleted → delete all Products
        related_name="products",
        null=True
    )
    stock = models.PositiveIntegerField(default=0)
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.SET_NULL,         
        null=True,
        related_name="products"
    )
    description = models.TextField(blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    barcode = models.CharField(max_length=100, blank=True, null=True)
    reorder_level = models.IntegerField(default=10)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"
