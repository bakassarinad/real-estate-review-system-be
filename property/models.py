from django.db import models

from cities_light.abstract_models import (
    AbstractCity, AbstractRegion, AbstractCountry, AbstractSubRegion
)
from cities_light.receivers import connect_default_signals
# from images.models import ImageAlbum
from users.models import LandlordProfile
from django.core.validators import MinValueValidator


class EnabledObjectManager(models.Manager):
    def get_queryset(self):
        return super(EnabledObjectManager, self).get_queryset().filter(enabled=True)


class Country(AbstractCountry):
    enabled = models.BooleanField(default=False)
    included_objects = EnabledObjectManager()
    objects = models.Manager()


connect_default_signals(Country)


class Region(AbstractRegion):
    enabled = models.BooleanField(default=False)
    included_objects = EnabledObjectManager()
    objects = models.Manager()


connect_default_signals(Region)


class SubRegion(AbstractSubRegion):
    enabled = models.BooleanField(default=False)
    included_objects = EnabledObjectManager()
    objects = models.Manager()


connect_default_signals(SubRegion)


class City(AbstractCity):
    enabled = models.BooleanField(default=False)
    timezone = models.CharField(max_length=40)
    included_objects = EnabledObjectManager()
    objects = models.Manager()

    def __str__(self):
        return f"{self.name}"


connect_default_signals(City)


class Property(models.Model):
    landlord = models.ForeignKey(LandlordProfile, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=150)
    address = models.TextField()
    description = models.TextField(null=True, blank=True)
    building_type = models.CharField(max_length=255, null=True, blank=True)
    overall_floors = models.PositiveIntegerField(null=True, blank=True)
    floor = models.PositiveIntegerField(null=True, blank=True)
    decoration = models.BooleanField(null=True, blank=True)
    overall_square = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0.0)])
    living_square = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0.0)])
    kitchen_square = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0.0)])
    view = models.CharField(max_length=255, null=True, blank=True)
    balcony = models.BooleanField(null=True, blank=True)
    city = models.ForeignKey(City, related_name='city', on_delete=models.CASCADE, blank=True, null=True)
    # album = models.OneToOneField(ImageAlbum, related_name='model', on_delete=models.CASCADE, blank=True, null=True)
    images = models.ManyToManyField('images.Image', related_name='properties', blank=True)

    def __str__(self):
        return f"{self.name} | {self.city}"
