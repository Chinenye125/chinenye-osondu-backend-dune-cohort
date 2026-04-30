from django.shortcuts import redirect, render, get_object_or_404
from .models import Product, Category
from .forms import ProductForm
from django.db.models import Count
from django.contrib import messages

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
    
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product_name = product.name
        product.delete()
        messages.success(request, f'{product_name} deleted successfully.')
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})





