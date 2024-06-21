from django.db import models
from datetime import date

# Create your models here.
    
class Inventory(models.Model):
    "Data structure of Items in database. Each item has a supplier and details eg. Name, description, price and date_created, supplier"
    name = models.CharField(max_length=15, default=None)
    description = models.TextField(max_length=100, default=None)
    price = models.FloatField(max_length=None, default=None)
    date_created = models.CharField(max_length=20, default=date.today())   
     
    def __str__(self) -> str:
        return f"Item: {self.name} | Price: {self.price}"
    
class Supplier(models.Model):
    """Data structure of Supplier record in database...name, email, phone number"""
    name = models.CharField(max_length=15, default=None)
    email = models.EmailField(max_length=100, default=None)
    phone_number = models.CharField(max_length=12, default=None)
    address = models.CharField(max_length=30, default=None)
    item_supplied = models.ManyToManyField(Inventory, related_name='suppliers')
    def __str__(self) -> str:
        return f"{self.name}"