from django.contrib import admin
from .models import Favorites, FavoritesItem

admin.site.register(Favorites)
admin.site.register(FavoritesItem)

