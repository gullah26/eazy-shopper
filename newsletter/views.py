from django.contrib import messages
from django.shortcuts import render
from .models import NewsletterUser
from .forms import UserSignUpForm


def newsletter_signup(request):
    form = UserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(request, 'Email already exists in database',
                            "alert alert-warning alert-dismissible")
        else:
            instance.save()
            messages.success(request, 'Email submitted to database',
                            "alert alert-success alert-dismissible")

    context = {
        'form': form,
    }
    template = "newsletter/sign_up.html"
    return render(request, template, context)


def newsletter_unsubscribe(request):
    form = UserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            messages.success(request, 'Email removed from database',
                                "alert alert-success alert-dismissible")

        else:
            messages.warning(request, 'Email not in database',
                             "alert alert-alert alert-dismissible")

    context = {
        'form': form,
    }
    template = "newsletter/unsubscribe.html"
    return render(request, template, context)
