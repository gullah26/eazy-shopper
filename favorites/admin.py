from django.contrib import admin
from .models import Favorite, FavoriteItem

admin.site.register(Favorite)
admin.site.register(FavoriteItem)
