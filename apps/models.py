from django.db import models
from django.db.models import Model, CharField


class Bolajon(Model):
    instagram = CharField(max_length=40)
    telegram  = CharField(max_length=40)
    phone_number = models.CharField(max_length=20)
    latitude = models.DecimalField(max_digits=9,decimal_places=6)
    longitude = models.DecimalField(max_digits=9,decimal_places=6)


