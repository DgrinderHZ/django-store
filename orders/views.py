from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required

from .utils import send_order_email
from .forms import OrderForm
from .models import Order


# Create your views here.
@login_required
def order(request):
    user = request.user

    if not user.cart.items.exists():
        return redirect('products_list')

    if request.method == 'GET':
        form = OrderForm()
    else:
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(user)
            send_order_email(user, order)
            return render(request, 'orders/order_success.html')

    return render(request,
                  'orders/order_form.html',
                  {'form': form})


@login_required
def show_user_orders(request):
    user = request.user
    orders = get_list_or_404(Order, user=user)
    return render(request, 'orders/orders_list.html', {'orders': orders})


def orders_list(request):
    user = request.user
    if user.is_authenticated and user.is_superuser:
        orders = get_list_or_404(Order)
        return render(request, 'orders/orders.html', {'orders': orders})
    return redirect('products_list')
