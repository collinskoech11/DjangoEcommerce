from django.db import models

# Create your models here.
class Products(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)

class Order(models.Model):
    def __str(self):
        return self.items
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.CharField(max_length=200)

class Sale(models.Model):
    buyer_name = models.CharField(max_length=200)
    sale_type = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    subtotal = models.CharField(max_length=200)