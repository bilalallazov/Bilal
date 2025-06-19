from django.core.management.base import BaseCommand
from store.models import Product
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Гарантирует, что у всех товаров есть корректный slug'

    def handle(self, *args, **kwargs):
        updated = 0
        for product in Product.objects.all():
            if not product.slug:
                product.slug = slugify(product.name)
                product.save()
                updated += 1
        self.stdout.write(self.style.SUCCESS(f'Обновлено товаров: {updated}')) 