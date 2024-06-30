from rest_framework import serializers
from .models import Inventory, Supplier


class InventorySerializer(serializers.ModelSerializer):
    suppliers = serializers.SerializerMethodField()
    class Meta:
        model = Inventory
        fields = '__all__'
    def get_suppliers(self, obj):
        return [supplier.name for supplier in obj.suppliers.all()]

class SupplierSerializer(serializers.ModelSerializer):
    items_supplied = serializers.SerializerMethodField()
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'email', 'phone_number', 'address', 'items_supplied']
    def get_items_supplied(self, obj):
        return [item.name for item in obj.item_supplied.all()]
