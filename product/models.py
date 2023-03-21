from django.db import models


# Create your models here.

class Product(models.Model):
    """
    this contains info on what a product should contain
    """
    title = models.CharField(max_length=250)
    # the minimum of 1000 chars
    description = models.CharField(max_length=250)
    # this enables us to have digit with more than 20  digits and in two decimal places
    price = models.DecimalField(max_digits=20, decimal_places=2)
    inventory_quantity = models.IntegerField(default=0)
