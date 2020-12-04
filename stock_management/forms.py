from django import forms
from .models import Fournisseur, Produit, Order, MergedOrder, OrderItems


class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = '__all__'


class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = '__all__'


class OrderItemsForm(forms.ModelForm):
    class Meta:
        model = OrderItems
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(format='%m/%d/%Y',
                                    attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        }


class MergedOrderForm(forms.ModelForm):
    class Meta:
        model = MergedOrder
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(format='%m/%d/%Y',
                                    attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        }
