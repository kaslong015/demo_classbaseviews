from email.headerregistry import Address
from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    age = models.IntegerField()
    Address = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name
