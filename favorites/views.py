from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from products.models import Product
from .models import Favorites


@login_required
def favorites(request):
    """
    This view renders user favorites
    """
    favorites = None
    try:
        favorites = Favorites.objects.get(user=request.user)
    except Favorites.DoesNotExist:
        pass

    context = {
        'favorites': favorites,
    }

    return render(request, 'favorites/favorites.html', context)


@login_required
def add_to_favorites(request, product_id):
    """
    Add a product to favorites
    for user that is logged in
    """
    product = get_object_or_404(Product, pk=product_id)

    # Create a favorites for the user if they don't have one
    favorites, _ = Favorites.objects.get_or_create(user=request.user)
    # Add product to the favorites
    favorites.products.add(product)
    messages.info(request, "A new product was added to your favorites")

    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_favorites(request, product_id):
    """
    Add a product from the store to the
    favorites for the logged in user
    """
    favorites = Favorites.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    # Remove product from the favorites
    favorites.products.remove(product)
    messages.info(request, "A product was removed from your favorites")

    return redirect(request.META.get('HTTP_REFERER'))