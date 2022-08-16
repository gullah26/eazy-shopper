from django.urls import path
from . import views

urlpatterns = [
    path('', views.favorites, name='favorites'),
    path(
        'add_to_favorites/<product_id>',
        views.add_to_favorites,
        name='add_to_favorites'),
    path(
        'remove_from_favorites/<product_id>',
        views.remove_from_favorites,
        name='remove_from_favorites'),
    
]
