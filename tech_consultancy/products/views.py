from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def home(request):
    categories = Category.objects.all()
    return render(request, 'products/home.html', {'categories': categories})

def product_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    return render(request, 'products/product_list.html', {'category': category, 'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})
