from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

from .forms import ContactForm


def contact(request):
    """A view to submit the form and send to customer support"""

    if request.method == "POST":
        form = Contact(request.POST)
        if form.is_valid():
            customer_email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            
            body = {
                "name": form.cleaned_data["full_name"],
                "email": form.cleaned_data["email"],
                "subject": form.cleaned_data["subject"],
                "message": form.cleaned_data["message"],
            }
            template = "contact/contact.html"
            return render(request, template)
            
    form = ContactForm()
    template = "contact/contact.html"
    context = {
        "form": form,
    }
    return render(request, template, context)
