# Generated by Django 5.1.6 on 2025-03-06 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payout_tracking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='delivery_aggregator',
            field=models.CharField(choices=[('glovo', 'Glovo'), ('wolt', 'Wolt'), ('choco', 'Chocofood'), ('yandex', 'yandex'), ('abr', 'abr')], default='wolt', max_length=10),
        ),
    ]
