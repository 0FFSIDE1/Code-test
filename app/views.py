from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView
from .models import Inventory, Supplier
from .serializers import InventorySerializer, SupplierSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib import messages
from rest_framework import status
# Create your views here.

class IndexPageView(ListView):
    queryset = Inventory.objects.all()
    template_name = 'app/index.html'
    context_object_name = 'items'

class Detailview(DetailView):
    """This displays items in the Inventory, list of items in database and their suppliers"""
    queryset = Inventory
    template_name = 'app/item_detail.html'
    context_object_name = 'items'
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
    def get_queryset(self):
        try:
            Inventory.objects.filter(pk=self.kwargs['pk'])
        except Inventory.MultipleObjectsReturned:
            return Inventory.objects.filter(pk=self.kwargs['pk'])
        finally:
            return Inventory.objects.filter(pk=self.kwargs['pk'])


def CreateSupplier(request):
    "This handles form submission for creating a supplier"
    if request.method == 'POST':
        supplier = Supplier.objects.create(
            name= request.POST['name'],
            email= request.POST['email'],
            phone_number= request.POST['telephone'],
            address= request.POST['address'],
        ) 
        # Get the data and save it create a new supplier in the database
        supplier.save()
        messages.success(request, 'Supplier created Successfully!') 
        return redirect('create-supplier')
    else:
        context = {
            'suppliers': Supplier.objects.all(),
        }
        return render(request, 'app/supplier.html', context)

def CreateInventory(request):
    """This creates an item in the Inventory if POST request is sent, else displays list of items in database and their suppliers"""
    if request.method == 'POST':
        item = Inventory.objects.create(
            name = request.POST['name'],
            price = request.POST['price'],
            date_created = request.POST['date'],
            description =request.POST['description'],
        )
        supplier = request.POST.getlist('supplier')
        item.suppliers.set(supplier)
        item.save()
        messages.success(request, 'Label created Successfully!')
        return redirect('create-inventory')
    
    else:
        context = {
        'suppliers': Supplier.objects.all(),
        'items': Inventory.objects.all(),
        
        }
        return render(request, 'app/inventory.html', context=context)


class SupplerDetail(DetailView):
    """This displays specific supplier in the Inventory, list of items supplier has in database"""
    queryset = Supplier
    template_name = 'app/supplier_detail.html'
    context_object_name = 'supplier'
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
    def get_queryset(self):
        try:
            Supplier.objects.filter(pk=self.kwargs['pk'])
        except Supplier.MultipleObjectsReturned:
            return Supplier.objects.filter(pk=self.kwargs['pk'])
        finally:
            return Supplier.objects.filter(pk=self.kwargs['pk'])

def CreateSupplier(request):
    "This handles form submission for creating a supplier"
    if request.method == 'POST':
        supplier = Supplier.objects.create(
            name= request.POST['name'],
            email= request.POST['email'],
            phone_number= request.POST['telephone'],
            address= request.POST['address'],
        ) 
        # Get the date and save it create a new supplier in the database
        supplier.save()
        messages.success(request, 'Supplier created Successfully!') 
        return redirect('create-supplier')
    else:
        context = {
            'suppliers': Supplier.objects.all(),
        }
        return render(request, 'app/supplier.html', context)
    
def DeleteSupplier(request, pk):
    """This function deletes a Supplier from the Supplier database"""
    supplier = Supplier.objects.get(pk=pk)
    supplier.delete()
    context = {
        'success': True
    }
    messages.success(request, 'Supplier deleted successfully')
    return JsonResponse(context)

def UpdateSupplier(request):
    "This handles form submission for Updating a supplier"
    if request.method == 'POST':
        id = request.POST['id']
        data = Supplier.objects.get(pk=id)
        data.name = request.POST['name']
        data.phone_number = request.POST['telephone']
        data.email = request.POST['email']
        data.address = request.POST['address']
        data.save()
        messages.success(request, 'Update saved successfully')
        return redirect('create-supplier')
    return render(request, 'app/supplier.html')        

def CreateInventory(request):
    """This creates an item in the Inventory if POST request is sent, else displays list of items in database and their suppliers"""
    if request.method == 'POST':
        item = Inventory.objects.create(
            name = request.POST['name'],
            price = request.POST['price'],
            date_created = request.POST['date'],
            description =request.POST['description'],
        )
        supplier = request.POST.getlist('supplier')
        item.suppliers.set(supplier)
        item.save()
        messages.success(request, 'Label created Successfully!')
        return redirect('create-inventory')
    
    else:
        context = {
        'suppliers': Supplier.objects.all(),
        'items': Inventory.objects.all(),
        
        }
        return render(request, 'app/inventory.html', context=context)

def deleteItem(request, pk):
    """This function deletes an item from the inventory database"""
    item = Inventory.objects.get(pk=pk)
    item.delete()
    context = {
        'success': True
    }
    messages.success(request, 'Item deleted successfully')
    return JsonResponse(context)

def updateItem(request):
    "This handles form submission for Updating a item"
    if request.method == 'POST':
        id = request.POST['id']
        item = Inventory.objects.get(pk=id)
        item.name = request.POST['Item_name']
        item.description = request.POST['description']
        item.date_created = request.POST['date_created']
        item.price = request.POST['price']
        supplier = request.POST.getlist('supplier')
        item.suppliers.set(supplier)
        item.save()
        messages.success(request, 'Update saved successfully')
        return redirect('create-inventory')
    return render(request, 'app/inventory.html')

def CreateSupplier(request):
    "This handles form submission for creating a supplier"
    if request.method == 'POST':
        supplier = Supplier.objects.create(
            name= request.POST['name'],
            email= request.POST['email'],
            phone_number= request.POST['telephone'],
            address= request.POST['address'],
        ) 
        # Get the date and save it create a new supplier in the database
        supplier.save()
        messages.success(request, 'Supplier created Successfully!') 
        return redirect('create-supplier')
    else:
        context = {
            'suppliers': Supplier.objects.all(),
        }
        return render(request, 'app/supplier.html', context)
    
def CreateInventory(request):
    """This creates an item in the Inventory if POST request is sent, else displays list of items in database and their suppliers"""
    if request.method == 'POST':
        item = Inventory.objects.create(
            name = request.POST['name'],
            price = request.POST['price'],
            date_created = request.POST['date'],
            description =request.POST['description'],
        )
        supplier = request.POST.getlist('supplier')
        item.suppliers.set(supplier)
        item.save()
        messages.success(request, 'Label created Successfully!')
        return redirect('create-inventory')
    
    else:
        context = {
        'suppliers': Supplier.objects.all(),
        'items': Inventory.objects.all(),
        
        }
        return render(request, 'app/inventory.html', context=context)

#
#  Api Views 
#  This view controls all the API calls, icludes view to view all items, to view specific items, to, DELETE,POST,GET,PUT,PATCH, also View all supplier and a specific supplier and their products

class AllItemDetailView(APIView):
    """To view all Products in the database"""
    def get(self, request):
        items = Inventory.objects.all() # This gets all the record of items in the database

        serializer = InventorySerializer(items, many=True)
        return Response(serializer.data)
        
    def delete(self, request, pk):
        """To delete specific items using a name of the item"""
        item = get_object_or_404(Inventory, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def post(self, request):
        """To Update entire details of a specific items using name of the item"""
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        """To Update specific field of a product using a name of the item to get the item"""
        item = get_object_or_404(Inventory, pk=pk) 
        serializer = InventorySerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
class ItemDetailView(APIView):
    def get(self, request, pk):
        """To get specific items using a pk of the item"""
        try:
            item = get_object_or_404(Inventory, pk=pk)
        except Inventory.MultipleObjectsReturned:
            item = Inventory.objects.filter(pk=pk)
        finally:
            serializer = InventorySerializer(item)
            return Response(serializer.data)
        
    def delete(self, request, pk):
        """To delete specific items using a name of the item"""
        item = get_object_or_404(Inventory, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        """To Update entire details of a specific items using name of the item"""
        item = get_object_or_404(Inventory, pk=pk)
        serializer = InventorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        """To Update specific field of a product using a name of the item to get the item"""
        item = get_object_or_404(Inventory, pk=pk) 
        serializer = InventorySerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SupplierView(APIView):
    """To view all suppliers and there products"""
    def get(self, request):
        items = Supplier.objects.all() #This gets all the supplier record in the database
        serializer = SupplierSerializer(items, many=True)
        return Response(serializer.data)
      
    def post(self, request):
        """Add suppliers"""
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """To delete specific items using a name of the item"""
        item = get_object_or_404(Supplier, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        """To Update entire details of a specific items using name of the item"""
        item = get_object_or_404(Supplier, pk=pk)
        serializer = SupplierSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        """To Update specific field of a product using a name of the item to get the item"""
        item = get_object_or_404(Supplier, pk=pk) 
        serializer = SupplierSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SupplierDetailView(APIView):
    """To view a specific supplier and product supplied"""
    def get(self, request, pk):
        items = Supplier.objects.filter(pk=pk) # This gets a specific supplier using the pk of the supplier
        serializer = SupplierSerializer(items, many=True)
        return Response(serializer.data)
   
    def delete(self, request, pk):
        """To delete specific supplier using a pk of the supplier"""
        item = get_object_or_404(Inventory, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        """To Update entire details of a specific Supplier"""
        item = get_object_or_404(Supplier, pk=pk)
        serializer = SupplierSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        """To Update specific field of a Supplier"""
        item = get_object_or_404(Supplier, pk=pk) 
        serializer = SupplierSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
