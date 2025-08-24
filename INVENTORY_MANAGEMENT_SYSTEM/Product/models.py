from django.db import models

# Create your models here.
from django.db import models
from Suppliers.models import Supplier  # if you have a supplier app

class Product(models.Model):
    sku = models.CharField(max_length=50, unique=True)  # Product ID / SKU
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="products")
    
    quantity_in_stock = models.IntegerField(default=0)
    reorder_level = models.IntegerField(default=10)
    
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    barcode = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
