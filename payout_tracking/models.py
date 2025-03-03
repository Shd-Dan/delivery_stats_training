from django.db import models


# Create your models here.

class Delivery(models.Model):
    date = models.DateField()
    sum_payout = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Delivery {self.delivery_id} - {self.date} - {self.sum_payout}"

