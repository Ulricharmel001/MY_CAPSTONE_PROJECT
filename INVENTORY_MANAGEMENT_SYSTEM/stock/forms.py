from django import forms
from .models import PurchaseOrder, SalesOrder

# ------------------------
# Purchase Form
# ------------------------
class PurchaseForm(forms.ModelForm):
    """
    Form for creating purchase orders.
    Uses Django ModelForm to auto-generate fields from PurchaseOrder model.
    """
    class Meta:
        model = PurchaseOrder
        fields = ["product", "store", "quantity", "unit_price"]


# ------------------------
# Sales Form
# ------------------------
class SalesForm(forms.ModelForm):
    """
    Form for creating sales orders.
    Uses Django ModelForm to auto-generate fields from SalesOrder model.
    """
    class Meta:
        model = SalesOrder
        fields = ["product", "store", "quantity", "unit_price"]
