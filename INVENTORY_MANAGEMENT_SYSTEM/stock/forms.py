from django import forms
from .models import Stock, StockTransaction

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["product", "store", "quantity"]
        widgets = {
            "product": forms.Select(attrs={"class": "form-control"}),
            "store": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
        }

class StockTransactionForm(forms.ModelForm):
    class Meta:
        model = StockTransaction
        fields = ["product", "store", "transaction_type", "quantity", "reference"]
        widgets = {
            "product": forms.Select(attrs={"class": "form-control"}),
            "store": forms.Select(attrs={"class": "form-control"}),
            "transaction_type": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
            "reference": forms.TextInput(attrs={"class": "form-control"}),
        }
