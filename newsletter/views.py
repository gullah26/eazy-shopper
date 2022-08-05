from django.shortcuts import render

# Create your views here.

def newsletter(request):
    """ A view to return the index page """
    return render(request, 'newsletter/newsletter.html')