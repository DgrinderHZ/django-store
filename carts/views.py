from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

# Create your views here.
from .models import Cart
from products.models import Product


@login_required
def cart(request):
    user = request.user
    products = user.cart.items.all()
    total_price = products.aggregate(total_price=Sum('price'))['total_price']
    return render(request, 
                  'carts/cart.html',
                  {
                      'products': products,
                      'total_price': total_price
                  })


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart.objects.get(user=request.user)
    cart.items.add(product)

    return redirect('cart')


@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart.objects.get(user=request.user)
    cart.items.remove(product)

    return redirect('cart')


@login_required
def remove_all_from_cart(request):
    products = get_list_or_404(Product)
    cart = Cart.objects.get(user=request.user)
    for product in products:
        cart.items.remove(product)

    return redirect('cart')
