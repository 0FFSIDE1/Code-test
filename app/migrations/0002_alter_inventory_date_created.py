# Generated by Django 5.0.6 on 2024-06-20 10:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 20, 10, 39, 51, 249101, tzinfo=datetime.timezone.utc)),
        ),
    ]
