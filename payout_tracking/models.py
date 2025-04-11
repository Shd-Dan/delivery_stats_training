from django.db import models
from django.db.models import ManyToManyField, CharField
from django.core.validators import MinLengthValidator


# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=40, validators=[MinLengthValidator(3, message='psssst!')])
    feedback = models.TextField()
    rating = models.PositiveIntegerField()


class BagColor(models.Model):
    bag_color = models.CharField(max_length=20)
    bag_number = models.IntegerField()

    def __str__(self):
        return f"{self.bag_color} - {self.bag_number}"


class Client(models.Model):
    client_email = models.EmailField(blank=True)
    client_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.client_name} - {self.client_email}"


# The class Courier is an illustration of many-to-many relationship
class Courier(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    GENDER_CHOICES = [
        (MALE, 'Man'),
        (FEMALE, 'Woman')
    ]

    courier_first_name = models.CharField(max_length=100)
    courier_last_name = models.CharField(max_length=100)
    courier_gender = models.CharField(max_length=7, choices=GENDER_CHOICES, default=MALE)
    bag = models.OneToOneField(BagColor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.courier_first_name} {self.courier_last_name}"


class Delivery(models.Model):
    wolt = 'wolt'
    glovo = 'glovo'
    choco = 'choco'
    yandex = 'yandex'
    abr = 'abr'

    DELIVERY_AGGREGATORS = [
        (glovo, 'Glovo'),
        (wolt, 'Wolt'),
        (choco, 'Chocofood'),
        (yandex, 'YandexEda'),
        (abr, 'abr+')
    ]

    date = models.DateField()
    sum_payout = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_id = models.CharField(max_length=100, unique=True)
    delivery_aggregator = models.CharField(
        max_length=10,
        choices=DELIVERY_AGGREGATORS,
        default='Wolt')
    delivery_items = models.CharField(max_length=50, blank=True)
    client = models.ForeignKey(Client, on_delete=models.PROTECT, null=True)

    # Many-to-Many relationship with Courier
    couriers = ManyToManyField(Courier, related_name='deliveries_related')

    def __str__(self):
        return f"Delivery {self.delivery_id} - {self.date} - {self.sum_payout}"
