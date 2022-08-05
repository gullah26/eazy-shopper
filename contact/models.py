from django.db import models


class Contact(models.Model):
    """ A model to save the contact form to the db """

    full_name = models.CharField(max_length=55,  blank=False)
    email = models.EmailField(max_length=254,  blank=False)
    subject = models.CharField(max_length=55, blank=False)
    message = models.CharField(max_length=1000, blank=False)

    def __str__(self):
        return self.full_name
