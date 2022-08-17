from django.shortcuts import render
from .models import NewsletterUser
from .forms import UserSignUpForm


def newsletter_signup(request):
    form = UserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            print("Email already exists")
        else:
            instance.save()

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

        else:
            print("Sorry email not found")

    context = {
        'form': form,
    }
    template = "newsletter/unsubscribe.html"
    return render(request, template, context)
