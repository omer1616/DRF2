from django.db import models


# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
