# Generated by Django 5.1.6 on 2025-04-07 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payout_tracking', '0012_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='surname',
        ),
    ]
