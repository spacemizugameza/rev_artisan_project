# Generated by Django 4.0.3 on 2022-04-19 13:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_alter_cart_quantity_alter_product_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 19, 19, 13, 27, 147488), editable=False),
        ),
    ]
