from django.contrib import admin
from django.db.models import QuerySet

from .models import Delivery, Client, Courier

# Register your models here.
admin.site.register(Client)
admin.site.register(Courier)


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ["delivery_id", "sum_payout", "delivery_aggregator", "delivery_items", "client"]
    list_editable = ["sum_payout", "delivery_aggregator", "delivery_items", "client"]
    filter_horizontal = ['couriers']
    list_per_page = 5
    actions = ['set_aggregator']
    search_fields = ['delivery_aggregator']

    @admin.action(description="Selecting aggregator of a delivery")
    def set_aggregator(self, request, qs: QuerySet):
        qs.update(delivery_aggregator=Delivery.wolt)
        self.message_user(
            request,
            f"{qs.update(delivery_aggregator=Delivery.wolt)} entries updated"
        )



""" method is an alternative to decorator
admin.site.register(Delivery, DeliveryAdmin)
"""