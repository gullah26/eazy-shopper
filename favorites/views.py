from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from products.models import Product
from .models import Favorite


@login_required
def favorite(request):
    """
    A view to render favorite
    """
    favorite = None
    try:
        favorite = Favorite.objects.get(user=request.user)
    except Favorite.DoesNotExist:
        pass

    context = {
        'favorite': favorite,
    }

    return render(request, 'favorite/favorite.html', context)


@login_required
def add_to_favorite(request, product_id):
    """
    Add item from the store to the
    favorite for an authenticated user
    """
    product = get_object_or_404(Product, pk=product_id)

    # Create a favorite for the user if they don't have one
    favorite, _ = Favorite.objects.get_or_create(user=request.user)
    # Add product to the favorite
    favorite.products.add(product)
    messages.info(request, "A new product was added to your favorite")

    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_favorite(request, product_id):
    """
    remove item from favorite for authenticated user
    """
    favorite = Favorite.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    # Removes item from favorite list
    favorite.products.remove(product)
    messages.info(request, "Item was removal successful")

    return redirect(request.META.get('HTTP_REFERER'))
