from django.shortcuts import render

from .models import *
# Create your views here.

def products_list(request):
    products = Products.objects.all()
    params = {'products': products}
    return render(request, 'products-list.html', params)



