from django.db import models
from concurrency.fields import AutoIncVersionField


# very simple product model
class Product(models.Model):
    # this field is for optimistic locking
    version = AutoIncVersionField()
    name = models.CharField(max_length=200, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True)


# this stores our results
class ProductJson(models.Model):
    # this field is for optimistic locking
    version = AutoIncVersionField()
    # contains the json data, can be optimized with specific libraries, but for simplicity we'll use text
    data = models.TextField()
    # updated every time save() is called on the model
    last_modified = models.DateTimeField(auto_now=True)
    # each ProductJson has exactly on Product
    product = models.OneToOneField(Product, related_name='product_json')
