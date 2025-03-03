from django import forms

from .models import Delivery


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['date', 'delivery_id', 'sum_payout']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'delivery_id': forms.TextInput(attrs={'class': 'form-control'}),
            'sum_payout': forms.NumberInput(attrs={'class': 'form-control'})
        }
