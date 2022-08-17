from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Favorite(models.Model):
    """
    Model to show all product items within the users favorites
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,
                                      through="favoriteItem",
                                      related_name='product_favorite')

    def __str__(self):
        return f'Favorite ({self.user})'


class FavoriteItem(models.Model):
    """
    A 'through' model, allowing users to add
    individual products to their favorite.
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
