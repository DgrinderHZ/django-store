from django.shortcuts import render, get_object_or_404

from .models import *
# Create your views here.

def products_list(request):
    products = Products.objects.all()
    params = {'products': products}
    return render(request, 'products/products-list.html', params)

def products_details(request, pk):
    product = get_object_or_404(Products, pk=pk)
    params = {'product': product}
    return render(request, 'products/product-details.html', params)



