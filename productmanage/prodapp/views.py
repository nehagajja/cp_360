# views.py
from rest_framework import viewsets
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
import csv
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

def export_products_csv(request):
    # Create the HttpResponse object with CSV header
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=products.csv'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Name', 'Description', 'Price', 'Category','Status','Created_at','Expiry_Date','Uploaded_By'])

    products = Product.objects.all()
    for product in products:
        writer.writerow([product.id, product.name, product.description, product.price, product.category.name,product.status,product.created_at,product.expiry_date,product.uploaded_by])

    return response

def home_view(request):
    #if request.method == 'POST':
        #result = generate_dummy_data.delay()
        #return JsonResponse({'status': 'Task started', 'task_id': result.id})
    return render(request, 'home.html')
