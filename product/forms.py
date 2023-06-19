from django import forms
from .models import Customer

class CustomerAddForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields= [
            "name",
            "phone",
            "address",
            "email",
            "quantity",
            "product"
        ]