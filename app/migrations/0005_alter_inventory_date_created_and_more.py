# Generated by Django 5.0.6 on 2024-06-20 14:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_inventory_supplier_inventory_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='date_created',
            field=models.CharField(default=datetime.date(2024, 6, 20), max_length=20),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='supplier',
            field=models.ManyToManyField(null=True, related_name='items', to='app.supplier'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(default=None, max_length=15, verbose_name='Supplier'),
        ),
    ]
