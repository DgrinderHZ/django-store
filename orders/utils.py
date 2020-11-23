from django.template.loader import render_to_string


def send_order_email(request, user, products, total_price):
    subject = 'Order confirmation'
    message = render_to_string('orders/order_details.html',
                               {
                                   'total_price': total_price
                               })

    user.email_user(subject, message)
