# Generated by Django 5.1.6 on 2025-03-12 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payout_tracking', '0005_delivery_client_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_email', models.EmailField(blank=True, max_length=254)),
                ('client_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='client_email',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='client_name',
        ),
    ]
