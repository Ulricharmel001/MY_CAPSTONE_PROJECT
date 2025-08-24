from django.db import models
from inventory.models import Product, Store

# ----------------------
# Stock: Track quantity per store
# ----------------------
class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="stocks")
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="stocks")
    quantity = models.IntegerField(default=0)

    class Meta:
        unique_together = ('product', 'store')
        ordering = ['product']

    def __str__(self):
        return f"{self.product.name} - {self.quantity} in {self.store.name}"


# ----------------------
# StockTransaction: Record in/out movements
# ----------------------
class StockTransaction(models.Model):
    IN = "IN"
    OUT = "OUT"
    TRANSACTION_TYPES = [(IN, "Stock In"), (OUT, "Stock Out")]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="transactions")
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="transactions")
    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPES)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    reference = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.transaction_type} - {self.product.name} ({self.quantity})"
