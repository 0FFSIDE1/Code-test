# Generated by Django 5.0.6 on 2024-06-21 09:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_inventory_supplier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='supplier',
        ),
        migrations.AddField(
            model_name='supplier',
            name='item_supplied',
            field=models.ManyToManyField(related_name='suppliers', to='app.inventory'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='date_created',
            field=models.CharField(default=datetime.date(2024, 6, 21), max_length=20),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(default=None, max_length=15),
        ),
    ]