from django import forms


class ContactForm(forms.Form):
    """ Contact form for users to contact customer support """

    full_name = forms.CharField(max_length=55, required=True)
    email = forms.EmailField(max_length=254, required=True)
    subject = forms.CharField(max_length=55, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True, max_length=1000)
