from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Favorite(models.Model):
    """
    Displays all items in the user's favorite list
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,
                                      through="FavoriteItem",
                                      related_name='product_favorites')

    def __str__(self):
        return f'Favorite ({self.user})'


class FavoriteItem(models.Model):
    """
    Model that allows user to add item individually to the favorite list.
    """

    product = models.ForeignKey(Product,
                                null=False,
                                blank=False,
                                on_delete=models.CASCADE)
    favorite = models.ForeignKey(Favorite,
                                 null=False,
                                 blank=False,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
