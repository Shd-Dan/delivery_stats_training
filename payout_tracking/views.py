# Create your views here.
from django.db.models.aggregates import Avg, Max, Min, Sum, Count, Value
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView

from .forms import DeliveryForm, FeedbackForm
from .models import Delivery, Courier, Feedback


class FeedbackView(View):
    def get(self, request):
        form = FeedbackForm()
        return render(request, 'payout_tracking/feedback.html', {'form': form})

    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'payout_tracking/done.html', {'form': form})
        return render(request, 'payout_tracking/feedback.html', {'form': form})


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
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
    form = FeedbackForm()
    return render(request, 'payout_tracking/feedback.html', context={'form': form})


def update_feedback(request, feedback_id):
    feed = Feedback.objects.get(id=feedback_id)
    if request.method == "POST":
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            form.save()
            return redirect('feedback')
    else:
        form = FeedbackForm(instance=feed)
    return render(request, 'payout_tracking/feedback.html', context={'form': form})


class DoneView(View):
    def get(self, request):
        return render(request, 'payout_tracking/done.html')


# class ListFeedback(TemplateView):
#     template_name = 'payout_tracking/list_feedback.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['feedback_list'] = Feedback.objects.all()
#
#         return context


class ListFeedback(ListView):
    """ Gets list of feedbacks item by ListView """""
    template_name = 'payout_tracking/list_feedback.html'
    model = Feedback



# class DetailFeedback(TemplateView):
#     """ Detail view for a specific feedback item by TemplateView "" """
#     template_name = 'payout_tracking/detail_feedback.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         feedback_id = self.kwargs.get('id_feedback')
#         context['feedback'] = Feedback.objects.get(id=feedback_id)
#         return context


class DetailFeedback(DetailView):
    """ Detail view for a specific feedback item by DetailView class"" """""
    template_name = 'payout_tracking/detail_feedback.html'
    model = Feedback