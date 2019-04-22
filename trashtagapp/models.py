from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class TrashLocation(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=2560)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    