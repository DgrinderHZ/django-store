from django.template.loader import render_to_string


def send_order_email(user, order):
    subject = 'Order confirmed'
    message = render_to_string('orders/order_details.html',
                               {
                                   'user': user,
                                   'order': order
                               })

    user.email_user(subject, message)
