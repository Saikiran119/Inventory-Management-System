# 0002_create_order_model.py
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('inventory', '0001_initial'),  # Reference the previous migration file
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True)),
                ('product', models.ForeignKey(on_delete=models.CASCADE, to='inventory.product')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'inventory_order',  # Ensure this matches the table name you want
            },
        ),
    ]
