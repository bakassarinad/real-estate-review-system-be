from django.db import models
from django.contrib.auth.models import User


class BaseUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    dob = models.DateField(verbose_name='Date of birth')

    class Meta:
        abstract = True
