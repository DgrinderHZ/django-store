from django.shortcuts import render, get_object_or_404
from django.db.models import Sum

from .models import Order
from .utils import send_order_email
from accounts.models import UserProfile


# Create your views here.
def order(request):
    user = request.user
    user_address = get_object_or_404(UserProfile, user_id=user.id).address
    products = user.cart.items.all()
    order = Order.objects.create(address=user_address, user=user)
    total_price = products.aggregate(total_price=Sum('price'))['total_price']

    for item in products:
        order.items.add(item)
        user.cart.items.remove(item)

    send_order_email(request, user, products, total_price)

    return render(request,
                  'orders/order_success.html'
                  )
