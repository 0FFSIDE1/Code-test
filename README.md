# Django Inventory Management Documentation
# This documentation provides an overview of the views and functionality implemented in a Django-based inventory management application. It covers class-based views, function-based views, and API views using Django REST Framework.
# 
# Class-based Views
# IndexPageView
# Purpose: Displays a list of all inventory items.
# Queryset: Retrieves all records from the Inventory model.
# Template: app/index.html
# Context Object Name: items

# DetailView
# Purpose: Displays details of a specific inventory item, including its suppliers.
# Queryset: Uses the Inventory model.
# Template: app/item_detail.html
# Context Object Name: items
# Slug Field: pk
# Slug URL Kwarg: pk

# SupplierDetail
# Purpose: Displays details of a specific supplier and their items.
# Queryset: Uses the Supplier model.
# Template: app/supplier_detail.html
# Context Object Name: supplier
# Slug Field: pk
# Slug URL Kwarg: pk

# Function-based Views
# DeleteSupplier
# Purpose: Deletes a supplier from the database.
# Parameters: request, pk (primary key of the supplier)
# Response: JSON response with a success message.

# UpdateSupplier
# Purpose: Handles form submission for updating a supplier's details.
# Method: POST
# Response: Redirects to the 'create-supplier' page on success.

# deleteItem
# Purpose: Deletes an item from the inventory database.
# Parameters: request, pk (primary key of the item)
# Response: JSON response with a success message.

# updateItem
# Purpose: Handles form submission for updating an item's details.
# Method: POST
# Response: Redirects to the 'create-inventory' page on success.

# CreateSupplier
# Purpose: Handles form submission for creating a new supplier.
# Method: POST
# Response: Redirects to the 'create-supplier' page on success. If GET, renders the supplier form.

# CreateInventory
# Purpose: Handles form submission for creating a new inventory item. If GET, displays a list of items and suppliers.
# Method: POST
# Response: Redirects to the 'create-inventory' page on success. If GET, renders the inventory form with context.

# API Views
# AllItemDetailView
# Purpose: Retrieves all items in the inventory.
# Method: GET
# Response: JSON response with serialized data of all inventory items.

# ItemDetailView
# Purpose: Provides CRUD operations for specific inventory items.
# GET: Retrieves a specific item by primary key.
# DELETE: Deletes a specific item by primary key.
# PUT: Updates all details of a specific item.
# PATCH: Partially updates a specific item.

# SupplierView
# Purpose: Provides CRUD operations for suppliers.
# GET: Retrieves all suppliers and their products.
# DELETE: Deletes a specific supplier by primary key.
# PUT: Updates all details of a specific supplier.
# PATCH: Partially updates a specific supplier.

# SupplierDetailView
# Purpose: Provides CRUD operations for a specific supplier.
# GET: Retrieves a specific supplier by primary key.
# DELETE: Deletes a specific supplier by primary key.
# PUT: Updates all details of a specific supplier.
# PATCH: Partially updates a specific supplier.

# Models Used
# Inventory: Represents an item in the inventory.
# Supplier: Represents a supplier with its details and associated inventory items.
# Serializers Used
# InventorySerializer: Serializes the Inventory model.
# SupplierSerializer: Serializes the Supplier model.

# Dependencies
# Django: For handling views, models, templates, and messages.
# Django REST Framework (DRF): For creating API views and serializing data.
# JSON Response: For returning JSON responses in function-based views.
# Messages: For displaying success messages to users after operations like create, update, and delete.

# This documentation provides a comprehensive overview of the views and functionality implemented in the inventory management application. Each section explains the purpose and functionality of the views and how they interact with models and templates.
