# Generated by Django 4.0.3 on 2022-04-01 10:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_cart_total_alter_product_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 1, 15, 39, 9, 469233), editable=False),
        ),
    ]
