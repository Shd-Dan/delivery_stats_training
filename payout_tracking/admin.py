from django.contrib import admin

from .models import Delivery


# Register your models here.
@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ["delivery_id", "sum_payout", ]
    list_editable = ["sum_payout", ]
    list_per_page = 5


""" method is an alternative to decorator
admin.site.register(Delivery, DeliveryAdmin)
"""