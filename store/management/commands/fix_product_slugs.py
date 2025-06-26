from django.core.management.base import BaseCommand
from store.models import Product
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Генерирует уникальные slug для всех товаров без slug и выводит их на экран'

    def handle(self, *args, **kwargs):
        updated = 0
        for product in Product.objects.filter(slug__isnull=True) | Product.objects.filter(slug=""):
            self.stdout.write(f'Товар без slug: id={product.id}, name={product.name}')
            base_slug = slugify(product.name)
            if not base_slug:
                base_slug = f"product-{product.id}"
            slug = base_slug
            counter = 1
            while Product.objects.filter(slug=slug).exclude(id=product.id).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            product.slug = slug
            product.save()
            self.stdout.write(self.style.SUCCESS(f'  -> Новый slug: {product.slug}'))
            updated += 1
        if updated == 0:
            self.stdout.write(self.style.WARNING('Все товары уже имеют slug!'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Обновлено товаров: {updated}'))

# Добавим скрипт для массовой замены картинки у товара по имени
def set_image_for_product(product_name, image_filename):
    product = Product.objects.filter(name__icontains=product_name).first()
    if product:
        product.image = f'картинки/{image_filename}'
        product.save()
        print(f'Картинка для "{product.name}" изменена на {image_filename}')
    else:
        print(f'Товар с именем "{product_name}" не найден!')

if __name__ == "__main__":
    set_image_for_product('Воздушный фильтр', 'аккумулятор.webp') 