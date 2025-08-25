from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Store, Category, Supplier, Customer, Product

# ----------------------
# Store Views
# ----------------------

@csrf_exempt
def store_list(request):
    """GET all stores or POST a new store"""
    if request.method == 'GET':
        stores = Store.objects.all()
        data = [{"id": s.id, "name": s.name, "location": s.location} for s in stores]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body)
        store = Store.objects.create(name=body['name'], location=body.get('location',''))
        return JsonResponse({"id": store.id, "name": store.name, "location": store.location}, status=201)

@csrf_exempt
def store_detail(request, pk):
    """GET, PUT, DELETE a single store"""
    store = get_object_or_404(Store, pk=pk)
    if request.method == 'GET':
        return JsonResponse({"id": store.id, "name": store.name, "location": store.location})
    elif request.method == 'PUT':
        body = json.loads(request.body)
        store.name = body.get('name', store.name)
        store.location = body.get('location', store.location)
        store.save()
        return JsonResponse({"id": store.id, "name": store.name, "location": store.location})
    elif request.method == 'DELETE':
        store.delete()
        return JsonResponse({"message": "Store deleted"}, status=204)


# ----------------------
# Category Views
# ----------------------

@csrf_exempt
def category_list(request):
    """GET all categories or POST a new category"""
    if request.method == 'GET':
        categories = Category.objects.all()
        data = [{"id": c.id, "name": c.name, "store": c.store.name} for c in categories]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body)
        store = get_object_or_404(Store, pk=body['store_id'])
        category = Category.objects.create(name=body['name'], store=store)
        return JsonResponse({"id": category.id, "name": category.name, "store": category.store.name}, status=201)

@csrf_exempt
def category_detail(request, pk):
    """GET, PUT, DELETE a single category"""
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'GET':
        return JsonResponse({"id": category.id, "name": category.name, "store": category.store.name})
    elif request.method == 'PUT':
        body = json.loads(request.body)
        category.name = body.get('name', category.name)
        category.save()
        return JsonResponse({"id": category.id, "name": category.name, "store": category.store.name})
    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({"message": "Category deleted"}, status=204)


# ----------------------
# Supplier Views
# ----------------------

@csrf_exempt
def supplier_list(request):
    """GET all suppliers or POST a new supplier"""
    if request.method == 'GET':
        suppliers = Supplier.objects.all()
        data = [{"id": s.id, "name": s.name, "email": s.email, "phone": s.phone} for s in suppliers]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body)
        supplier = Supplier.objects.create(
            name=body['name'],
            email=body.get('email'),
            phone=body.get('phone'),
            address=body.get('address','')
        )
        return JsonResponse({"id": supplier.id, "name": supplier.name}, status=201)

@csrf_exempt
def supplier_detail(request, pk):
    """GET, PUT, DELETE a single supplier"""
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'GET':
        return JsonResponse({"id": supplier.id, "name": supplier.name, "email": supplier.email, "phone": supplier.phone})
    elif request.method == 'PUT':
        body = json.loads(request.body)
        supplier.name = body.get('name', supplier.name)
        supplier.email = body.get('email', supplier.email)
        supplier.phone = body.get('phone', supplier.phone)
        supplier.save()
        return JsonResponse({"id": supplier.id, "name": supplier.name})
    elif request.method == 'DELETE':
        supplier.delete()
        return JsonResponse({"message": "Supplier deleted"}, status=204)


# ----------------------
# Customer Views
# ----------------------

@csrf_exempt
def customer_list(request):
    """GET all customers or POST a new customer"""
    if request.method == 'GET':
        customers = Customer.objects.all()
        data = [{"id": c.id, "name": c.name, "email": c.email} for c in customers]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body)
        customer = Customer.objects.create(
            name=body['name'],
            email=body.get('email'),
            phone=body.get('phone'),
            address=body.get('address','')
        )
        return JsonResponse({"id": customer.id, "name": customer.name}, status=201)

@csrf_exempt
def customer_detail(request, pk):
    """GET, PUT, DELETE a single customer"""
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'GET':
        return JsonResponse({"id": customer.id, "name": customer.name, "email": customer.email})
    elif request.method == 'PUT':
        body = json.loads(request.body)
        customer.name = body.get('name', customer.name)
        customer.email = body.get('email', customer.email)
        customer.save()
        return JsonResponse({"id": customer.id, "name": customer.name})
    elif request.method == 'DELETE':
        customer.delete()
        return JsonResponse({"message": "Customer deleted"}, status=204)


# ----------------------
# Product Views
# ----------------------

@csrf_exempt
def product_list(request):
    """GET all products or POST a new product"""
    if request.method == 'GET':
        products = Product.objects.all()
        data = [{"id": p.id, "name": p.name, "sku": p.sku, "category": p.category.name if p.category else None} for p in products]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body)
        category = get_object_or_404(Category, pk=body['category_id'])
        supplier = get_object_or_404(Supplier, pk=body['supplier_id'])
        product = Product.objects.create(
            sku=body['sku'],
            name=body['name'],
            category=category,
            supplier=supplier,
            unit_price=body['unit_price'],
            selling_price=body['selling_price']
        )
        return JsonResponse({"id": product.id, "name": product.name}, status=201)

@csrf_exempt
def product_detail(request, pk):
    """GET, PUT, DELETE a single product"""
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return JsonResponse({
            "id": product.id,
            "name": product.name,
            "sku": product.sku,
            "category": product.category.name if product.category else None,
            "supplier": product.supplier.name if product.supplier else None
        })
    elif request.method == 'PUT':
        body = json.loads(request.body)
        product.name = body.get('name', product.name)
        product.sku = body.get('sku', product.sku)
        product.save()
        return JsonResponse({"id": product.id, "name": product.name})
    elif request.method == 'DELETE':
        product.delete()
        return JsonResponse({"message": "Product deleted"}, status=204)
