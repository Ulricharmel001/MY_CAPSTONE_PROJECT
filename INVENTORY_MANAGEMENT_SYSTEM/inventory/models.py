from django.db import models
from django.conf import settings

# Store: Multiple store can be craete by a user, when a store is deleted every infor about the store would be deleted
class Store(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="stores"
    )
    name = models.CharField(max_length=100)
    location = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Category: Product categorization, store can have many categories
class Category(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="categories"
    )
    name = models.CharField(max_length=100)
    # product = models.ForeignKey(Product,)
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

# Supplier: Provides products,  from whom we are buying to refill our store
class Supplier(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="suppliers"
    )
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



#record info of customers, the person buying from  us

class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="customers"
    )
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

# Product: Inventory items :
#  "" item we sell , product has unit code sku""   
class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="products"
    )
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
    selling_price = models.FloatField()
    barcode = models.CharField(max_length=100, blank=True, null=True)
    reorder_level = models.IntegerField(default=10)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"
