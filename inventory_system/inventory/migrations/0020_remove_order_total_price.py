# Generated by Django 4.2.11 on 2025-01-30 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0019_order_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
    ]
