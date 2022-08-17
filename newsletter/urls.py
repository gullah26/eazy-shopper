from django.urls import path
from . import views

urlpatterns = [
    path('unsubscribe/', views.newsletter_unsubscribe, 
         name='newsletter_unsubscribe'),
    path('sign_up/', views.newsletter_signup, name='newsletter_signup'),
]
