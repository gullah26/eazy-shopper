from django.urls import path
from . import views

urlpatterns = [
    path('', views.favorite, name='favorite'),
    path(
        'add_to_favorite/<product_id>',
        views.add_to_favorite,
        name='add_to_favorite'),
    path(
        'remove_from_favorite/<product_id>',
        views.remove_from_favorite,
        name='remove_from_favorite'),
]
