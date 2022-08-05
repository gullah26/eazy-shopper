from django.db import models


class Newsletter(models.Model):
    """ A model to save the newsletter entry into the database """

    title = models.CharField(max_length=55,  blank=False)
    date = models.EmailField(max_length=25,  blank=False)
    entry = models.CharField(max_length=1000, blank=False)


    def __str__(self):
        return self.full_name