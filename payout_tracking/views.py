# Create your views here.
from django.db.models.aggregates import Avg, Max, Min, Sum, Count, Value
from django.shortcuts import render, redirect

from .forms import DeliveryForm
from .models import Delivery, Courier


def index(request):
    sort_param = request.GET.get('sort', '')

    if sort_param == 'date_asc':
        deliveries = Delivery.objects.order_by('date')
    elif sort_param == 'date_desc':
        deliveries = Delivery.objects.order_by('-date')
    elif sort_param == 'sum_payout_asc':
        deliveries = Delivery.objects.order_by('sum_payout')
    elif sort_param == 'sum_payout_desc':
        deliveries = Delivery.objects.order_by('-sum_payout')
    else:
        deliveries = Delivery.objects.annotate(
            true_bool=Value(True)
        )  # Get all deliveries from the database


    agg = Delivery.objects.all().aggregate(
        Avg('sum_payout'),
        Max('sum_payout'),
        Min('sum_payout'),
        Sum('sum_payout'),
        Count('sum_payout')
    )

    return render(request, 'payout_tracking/index.html',
                  context={'deliveries': deliveries,
                           'agg': agg}
                  )


def add_delivery(request):
    if request.method == "POST":
        form = DeliveryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeliveryForm()

    return render(request, 'payout_tracking/add_delivery.html', {'form': form})


def delivery_details(request, delivery_id):
    delivery = Delivery.objects.get(delivery_id=delivery_id)
    return render(request, 'payout_tracking/delivery_details.html', {'delivery': delivery})


def courier_details(request, courier):
    first_name = courier.split()[0]
    courier_get = Courier.objects.get(courier_first_name=first_name)
    return render(request, 'payout_tracking/courier_details.html', {'courier': courier_get})


def feedback(request):
    return render(request, 'payout_tracking/feedback.html')
