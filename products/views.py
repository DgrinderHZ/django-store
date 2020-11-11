from django.shortcuts import render, get_object_or_404

from .models import Product
# Create your views here.


def products_list(request):
    products = Product.objects.all()
    params = {'products': products}
    return render(request, 'products/products-list.html', params)


def products_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    params = {'product': product}
    return render(request, 'products/product-details.html', params)


def product_add(request):
    if request.method == 'POST':
        post = {'post': request.POST['title']}
        return render(request, "products/product-added.html", context=post)
    else:
        return render(request, "products/product-add.html")
