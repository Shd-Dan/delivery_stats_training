# Generated by Django 5.1.6 on 2025-03-06 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payout_tracking', '0003_delivery_delivery_items_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='client_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
