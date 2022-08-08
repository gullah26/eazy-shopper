from django.shortcuts import render

# Create your views here.


def shipping(request):
    """ A view to return the shipping and delivery page """
    return render(request, 'shipping/shipping.html')
