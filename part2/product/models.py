from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=240)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    title = models.TextField(max_length=150)
    price = models.IntegerField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name="products")
    created_date = models.DateField(auto_now_add=True)
    is_stock = models.BooleanField(verbose_name="Stok", default=True)
