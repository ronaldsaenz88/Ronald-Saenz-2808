# Generated by Django 3.1.7 on 2021-03-20 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currencyformat', '0002_worldcurrencyformat_display_currency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worldcurrencyformat',
            name='created_on',
        ),
    ]
