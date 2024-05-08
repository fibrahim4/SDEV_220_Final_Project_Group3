from django import forms

from .models import Inventory

class InventoryInput(forms.ModelForm):

    class Meta:
        model = Inventory
        fields = ('name', 'quantity', 'price', 'status',)