from django.db import models


class NewsletterUser(models.Model):
    """ A model to save the newsletter entry into the database """

    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

