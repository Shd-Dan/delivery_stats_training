# Generated by Django 5.1.6 on 2025-03-20 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payout_tracking', '0009_alter_delivery_delivery_aggregator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='couriers',
            field=models.ManyToManyField(related_name='deliveries_related', to='payout_tracking.courier'),
        ),
    ]
