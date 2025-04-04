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

class FeedbackForm(forms.Form):
    client_name = forms.CharField(max_length=100)
    feedback = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    rating= forms.IntegerField(min_value=1, max_value=5)
