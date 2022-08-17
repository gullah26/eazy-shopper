from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from products.models import Product
from .models import Favorite


@login_required
def favorite(request):
    """
    This view renders user favorite
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
    Add a product to favorite
    for user that is logged in
    """
    product = get_object_or_404(Product, pk=product_id)

    # Create a favorites for the user if they don't have one
    favorite, _ = Favorite.objects.get_or_create(user=request.user)
    # Add product to the favorites
    favorite.products.add(product)
    messages.info(request, "A new product was added to your favorite")

    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_favorite(request, product_id):
    """
    Add a product from the store to the
    favorite for the logged in user
    """
    favorite = Favorite.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    # Remove product from the favorite
    favorite.products.remove(product)
    messages.info(request, "A product was removed from your favorite")

    return redirect(request.META.get('HTTP_REFERER'))
