from django.contrib.auth.decorators import login_required 
from django.shortcuts import redirect, render, get_object_or_404 
from .models import Product, Category
from .forms import ProductForm
from django.db.models import Count   
from django.contrib import messages 
from rest_framework.views import APIView   
from rest_framework.response import Response  
from rest_framework import status  
import json
from django.http import JsonResponse
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .pagination import ProductPagination
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import IsOwnerOrReadOnly

def custom_404(request, exception):
    return render(request, '404.html', status=404)


def home(request):
    featured_products = Product.objects.all()[:3]
    return render(request, 'products/home.html', {
        'featured_products': featured_products
    })


def about(request):
    return render(request, 'products/about.html')


def product_list(request):
    query = request.GET.get('search')  # this is for the search input

    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    return render(request, 'products/product_list.html', {
        'products': products,
        'query': query
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {
        'product': product
    })


def category_list(request):
    categories = Category.objects.annotate(product_count=Count('products'))
    return render(request, 'products/category_list.html', {
        'categories': categories
    })

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    return render(request, 'products/product_list.html', {
        'products': products,
        'category': category
    })


@login_required
def product_create(request):
   if request.method == 'POST':
       form = ProductForm(request.POST)
       if form.is_valid():
          form.save()
          messages.success(request, 'Product added successfully.')
          return redirect('product_list')
   else:
        form = ProductForm()
        return render(request, 'products/product_form.html', {'form': form})
   
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
       form = ProductForm(request.POST, instance=product)
       if form.is_valid():
            form.save()
            messages.success(request, 'Product saved successfully.')
            return redirect('product_list')
    else:
       form = ProductForm(instance=product)
       return render(request, 'products/product_form.html', {'form': form})
    

"""Only logged-in staff users can delete products"""
@login_required
def product_delete(request, pk):
   product = get_object_or_404(Product, pk=pk)

# Restrict to staff (admins)
   if not request.user.is_staff:
       messages.error(request, "You are not authorized to delete this product.")
       return redirect('product_list')

   if request.method == 'POST':
      product_name = product.name
      product.delete()
      messages.success(request, f'{product_name} deleted successfully.')
      return redirect('product_list')

    # GET request > show confirmation page 
   return render(request, 'products/product_confirm_delete.html', {
      'product': product
})

def product_list_json(request):
    # fetch all products from the database
    products = Product.objects.all()
    # build a list of dicts - JSON cannot serialize Django Querystes directly
    data =[
        {
            'id' : p.id,
            'name': p.name,
            'price': str(p.price),  # Convert Decimal to string for JSON serialization
            'stock': p.stock,
            'is_available': p.is_available,
        }
        for p in products
    ]
    # JsonResponse convert the dict/list to JSON authomatically
    # safe-False is needed when returning a list instead of a dict
    return JsonResponse(data, safe=False)

def product_detail_json(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {
            'id': product.id,
            'name': product.name,
            'price': str(product.price),
            'stock': product.stock,
            'is_available': product.is_available,
        }
        return JsonResponse(data, safe=False)
    except Product.DoesNotExist:
        # return 404 status when the product is not found
        return JsonResponse(
        {'error': 'Product not found'},
        status=404
    )
   
"""List & Create API view"""
class ProductListAPIView(APIView):
   permission_classes = [IsAuthenticated]


   def get(self, request):
        products = Product.objects.all()
        # FILTERING
        category = request.GET.get('category')
        is_available = request.GET.get('is_available')
        search = request.GET.get('search')
        ordering = request.GET.get('ordering')

        if category:
            products = products.filter(category=category)

        if is_available:
            products = products.filter(is_available=is_available)

        if search:
            products = products.filter(name__icontains=search)

        if ordering:
            products = products.order_by(ordering)

             # PAGINATION (6 per page)
            paginator = ProductPagination()
            paginated_products = paginator.paginate_queryset(products, request)

            serializer = ProductSerializer(paginated_products, many=True)
        return paginator.get_paginated_response(serializer.data)
   
   def post(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# PRODUCT DETAIL (GET, PUT, DELETE)

class ProductDetailAPIView(APIView):

    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)

        # check ownership manually is still enforced by permission class
        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    # CATEGORY LIST
class CategoryListAPIView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
"""PRODUCT CREATE API VIEW"""
"""Only authenticated users can access the API views"""
"""Unuthorised requests will receive a 401 Unauthorized response automatically"""
class ProductCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





