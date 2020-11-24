from django.shortcuts import render
from django.db.models import Sum

from .utils import send_order_email
from .forms import OrderForm


# Create your views here.
def order(request):
    if request.method == 'GET':
        form = OrderForm()
    else:
        form = OrderForm(request.POST)
        user = request.user
        if form.is_valid():
            order = form.save()
            order.user = user

            products = user.cart.items.all()
            total_price = products.aggregate(
                total_price=Sum('price'))['total_price']

            for item in products:
                order.items.add(item)
                user.cart.items.remove(item)
            send_order_email(request, user, products, total_price)

            return render(request, 'orders/order_success.html')

    return render(request,
                  'orders/order_form.html',
                  {'form': form})
