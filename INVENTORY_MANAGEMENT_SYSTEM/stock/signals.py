from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import StockTransaction, Stock

@receiver(post_save, sender=StockTransaction)
def update_stock(sender, instance, created, **kwargs):
    """
    Automatically updates Stock quantity whenever a StockTransaction is created.
    """
    if not created:
        return  # Only act on new transactions

    product = instance.product
    store = instance.store

    # Get or create Stock record for this product and store
    stock, _ = Stock.objects.get_or_create(product=product, store=store)

    # Update quantity based on transaction type
    if instance.transaction_type == StockTransaction.IN:
        stock.quantity += instance.quantity
    elif instance.transaction_type == StockTransaction.OUT:
        stock.quantity -= instance.quantity

    stock.save()
