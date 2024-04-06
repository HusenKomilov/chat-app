from django.db import models

class Olx(models.Model):
    title = models.CharField(max_length=256)
    locations = models.CharField(max_length=256)
    price = models.CharField(max_length=128)
    url = models.CharField(max_length=128)

    def __str__(self):
        return self.title
