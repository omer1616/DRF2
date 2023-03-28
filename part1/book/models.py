from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(verbose_name="İsim", max_length=240)
    last_name = models.CharField(verbose_name="Soyisim", max_length=240)
    biography = models.TextField(verbose_name="Biyografi", max_length=400)


class Book(models.Model):
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE, related_name="books")
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
