from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):

        categories_list = [
            {'name': 'Умный дом', 'description': 'Товары для умного дома'},
            {'name': 'Техника для кухни', 'description': 'Крупная и мелкая кухонная техника'},
            {'name': 'Игры и софт', 'description': 'Игры и программы для пк'},
            {'name': 'Красота и здоровье', 'description': 'Укладка волос, бритье и стрижка'},
        ]

        categories_for_create = []

        for category_item in categories_list:
            categories_for_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(categories_for_create)

        product_list = [[{"name": "Яндекс станция", "description": "Умная колонка Яндекс Станция 2 с Алисой",
                          "category": Category.objects.get(pk=1),
                          "price_for_purchase": 16599, "creation_date": "2022-07-04",
                          "last_change_date": "2023-07-17"}]]

        products_to_create = []

        for product_item in product_list:
            products_to_create.append(
                Product(**product_item)
            )
        Product.objects.bulk_create(products_to_create)
