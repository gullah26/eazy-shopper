from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Favorites(models.Model):
    """
    Model to show all product items within the users favorites
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,
                                      through="favoritesItem",
                                      related_name='product_favorites')

    def __str__(self):
        return f'Favorites ({self.user})'


class FavoritesItem(models.Model):
    """
    A 'through' model, allowing users to add
    individual products to their favorites.
    """

    product = models.ForeignKey(Product,
                                null=False,
                                blank=False,
                                on_delete=models.CASCADE)
    favorites = models.ForeignKey(Favorites,
                                  null=False,
                                  blank=False,
                                  on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
