# Generated by Django 5.0.6 on 2024-06-20 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_inventory_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='supplier',
            field=models.ManyToManyField(related_name='items', to='app.supplier'),
        ),
    ]