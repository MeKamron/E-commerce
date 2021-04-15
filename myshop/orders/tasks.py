from celery import task
from django.core.mail import send_mail
from .models import Order
from decimal import Decimal

@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is 
    successfully placed
    """
    order = Order.objects.get(id=order_id)

    subject = f'Order no. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
            f'You have successfully placed an order.\n' \
            f'Your id is {order.id}\n' \
            f'Your total purchase is ${order.get_total_cost()}\n'

    mail_sent = send_mail(subject, message, 'kamronbek.abdumannonov.uz@gmail.com', [order.email])

    return mail_sent