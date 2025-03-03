# Create your views here.
from django.shortcuts import render, redirect

from .forms import DeliveryForm
from .models import Delivery


def index(request):
    deliveries = Delivery.objects.all()  # Get all deliveries from the database
    data = {
        "deliveries": deliveries
    }
    return render(request, 'payout_tracking/index.html', context=data)


def add_delivery(request):
    if request.method == "POST":
        form = DeliveryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeliveryForm()

    return render(request, 'payout_tracking/add_delivery.html', {'form': form})
