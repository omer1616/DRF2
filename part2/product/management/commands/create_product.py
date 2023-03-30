from django.core.management import BaseCommand
from ...models import Product, Category
import requests


class Command(BaseCommand):

    def handle(self, *args, **options):
        url = "https://dummyjson.com/products"

        response = requests.get(url)
        print(response.json())
        products = response.json()

        for product in products['products']:
            category = Category.objects.create(name=product['category'])
            Product.objects.create(
                name=product['title'],
                title=product['description'],
                price=product['price'],
                stock=product['stock'],
                brand=product['brand'],
                category=category,

            )
            print("--" * 25, "kaydedildi")



