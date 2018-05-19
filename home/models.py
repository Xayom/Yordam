from django.db import models


class Location(models.Model):
    city = models.CharField("Город ", max_length=30)
    country = models.CharField("Страна ", max_length=30)
    slug = models.SlugField()

    def __str__(self):
        return self.city