from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .utils import send_order_email
from .forms import OrderForm


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
