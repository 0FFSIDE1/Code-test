# Generated by Django 5.0.6 on 2024-06-20 10:36

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=15)),
                ('email', models.EmailField(default=None, max_length=100)),
                ('phone_number', models.CharField(default=None, max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=15)),
                ('description', models.TextField(default=None, max_length=100)),
                ('price', models.FloatField(default=None)),
                ('date_created', models.DateField(default=datetime.date(2024, 6, 20), max_length=15)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='app.supplier')),
            ],
        ),
    ]
