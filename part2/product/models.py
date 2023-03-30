from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=240)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=240)
    title = models.TextField(max_length=240)
    price = models.FloatField()
    stock = models.IntegerField(default=0)
    brand = models.CharField(max_length=240, default=None)
    created_date = models.DateField(auto_now_add=True)
    is_stock = models.BooleanField(verbose_name="Stok", default=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        return self.name
