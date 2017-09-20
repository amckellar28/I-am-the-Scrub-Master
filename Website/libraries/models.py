from django.db import models


class Library(models.Model):
    title = models.CharField(max_length = 140)
    address = models.TextField()
    number = models.IntegerField()
    emailaddress = models.EmailField(max_length=254)

    def __str__(self):
        return self.title
