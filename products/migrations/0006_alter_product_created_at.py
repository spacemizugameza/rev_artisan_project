# Generated by Django 4.0.3 on 2022-03-27 13:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_created_at_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 27, 19, 21, 9, 880604), editable=False),
        ),
    ]
