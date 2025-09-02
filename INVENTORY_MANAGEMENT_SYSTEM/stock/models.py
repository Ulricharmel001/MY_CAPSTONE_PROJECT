from django.db import models
from inventory.models import Product, Store


# ----------------------
# PurchaseOrder: Records when products are bought (stock in)
# ----------------------
class PurchaseOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)# product bought
    store = models.ForeignKey(Store, on_delete=models.CASCADE)# Store the product is going
    quantity = models.PositiveIntegerField() # amount bought and must be positive
    unit_price = models.FloatField() # price per product bought
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Purchase {self.product.name} x {self.quantity}"


# ----------------------
# SalesOrder: Records when products are sold (stock out)
# ----------------------
class SalesOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)# product sold
    store = models.ForeignKey(Store, on_delete=models.CASCADE)# store in charge, where the product leaving
    quantity = models.PositiveIntegerField() # quantity must be positive
    unit_price = models.FloatField()  # Price per unit (selling price to customer)
    date = models.DateTimeField(auto_now_add=True) # time of sales

    def __str__(self):
        return f"Sale {self.product.name} x {self.quantity}"
