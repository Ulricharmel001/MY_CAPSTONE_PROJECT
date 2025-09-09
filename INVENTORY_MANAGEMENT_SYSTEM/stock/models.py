from django.db import models
from inventory.models import Product, Store, Supplier, Customer
from django.conf import settings

# PurchaseOrder: Records when products are bought (stock in)
class PurchaseOrder(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  related_name="purchases"
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)# product bought
    store = models.ForeignKey(Store, on_delete=models.CASCADE)# Store the product is going
    quantity = models.PositiveIntegerField() # amount bought and must be positive
    unit_price = models.FloatField() # price per product bought
    date = models.DateTimeField(auto_now_add=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return f"Purchase {self.product.name} x {self.quantity}"

# SalesOrder: Records when products are sold (stock out)
class SalesOrder(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sales"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)# product sold
    store = models.ForeignKey(Store, on_delete=models.CASCADE)# store in charge, where the product leaving
    quantity = models.PositiveIntegerField() # quantity must be positive
    unit_price = models.FloatField()  # Price per unit (selling price to customer)
    date = models.DateTimeField(auto_now_add=True) # time of sales
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,blank=True, null= True )



    def __str__(self):
        return f"Sale {self.product.name} x {self.quantity}"
