from django.urls import path
from .views import DeleteSupplier, IndexPageView, CreateInventory, ItemDetailView, Detailview, CreateSupplier,  SupplierView, AllItemDetailView, SupplierDetailView, UpdateSupplier, deleteItem, updateItem, SupplerDetail


urlpatterns = [
    path('', IndexPageView.as_view(), name='index'), # Index page
    path('item/create', CreateInventory, name='create-inventory'), # Create an item in the inventory
    path('item/view/details/<int:pk>', Detailview.as_view(), name='details'), # view details of an item using item pk or id
    path('item/update', updateItem, name='update'), # update an item in the inventory
    path('item/delete/<int:pk>', deleteItem, name='delete-inventory'), # Delete an item in the inventory
    path('supplier/create', CreateSupplier, name='create-supplier'), # Create a supplier
    path('supplier/view/details/<int:pk>', SupplerDetail.as_view(), name='supplier-details'), # view details of a specific supplier using pk or id
    path('supplier/update', UpdateSupplier, name='update-supplier'), # Delete an item in the inventory
    path('supplier/delete/<int:pk>', DeleteSupplier, name='delete-supplier'), # Delete an item in the inventory


    # API URL
    path('api/supplier', SupplierView.as_view(), name="supplier-all"), #Api calls to view all supplier..... GET, POST, PUT, PATCH
    path('api/supplier/<int:pk>', SupplierDetailView.as_view(), name="supplier-specific"), #Api calls for a specific supplier.... GET, POST, PUT, PATCH
    path('api/items', AllItemDetailView.as_view(), name="all-item-detail"), #Api calls for all items .....GET, POST, PUT, PATCH
    path('api/items/<int:pk>', ItemDetailView.as_view(), name="item-detail"), #Api calls for items.... GET, POST, PUT, PATCH
]