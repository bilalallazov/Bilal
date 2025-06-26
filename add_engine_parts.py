import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carstore.settings')
django.setup()

from store.models import Category, Product

try:
    engine = Category.objects.get(slug='engine')
except Category.DoesNotExist:
    print("Категория 'Двигатель' (slug='engine') не найдена!")
    exit(1)

parts = [
    ('Вал коленчатый', 25000),
    ('Головка блока цилиндров', 18000),
    ('Ремень ГРМ', 2500),
    ('Ролик ГРМ', 1200),
    ('Ремень генератора', 900),
    ('Натяжной ролик', 1500),
    ('Система газораспределения', 8000),
    ('Система смазки двигателя', 6000),
    ('Шатун', 3500),
    ('Поршень', 2200),
    ('Кольца поршневые', 1100),
    ('Шкив', 1700)
]

for name, price in parts:
    product, created = Product.objects.get_or_create(
        category=engine,
        name=name,
        defaults={
            'price': price,
            'stock': 10,
            'available': True,
            'description': 'Тестовое описание'
        }
    )
    if not created:
        product.price = price
        product.save()
    print(('Добавлено' if created else 'Обновлено') + f': {name} — {price}₽') 