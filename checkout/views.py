from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LRb36Ft9uoJN92u5zOFBdD2oNtuHu7tHrouCuS967lCC0XptyvYc1wbF3W3mvTJ8SwvD8HRMyoUuajSSIsIVTR900LUiUzn9M',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
