import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carstore.settings')
django.setup()

from store.models import Product
from django.conf import settings

src_dir = os.path.join(settings.BASE_DIR, 'картинки')

# Ключевые слова для сопоставления
KEYWORDS = {
    'аккумулятор': 'аккумулятор.webp',
    'генератор': 'генератор.webp',
    'амортизатор': 'амартизаторы.webp',
    'пружина': 'пружина подвески.webp',
    'масляный': 'масляной фильтр.webp',
    'тормозной диск': 'тормрзные диски .webp',
    'тормоз': 'тормозные коллодки.webp',
    'диск': 'тормрзные диски .webp',
    'фара': 'фары.webp',
    'бампер': 'бампер.webp',
}

for product in Product.objects.all():
    found = False
    # 1. Поиск по слагу
    for ext in ['webp', 'jpg', 'jpeg', 'jfif', 'png']:
        filename = f"{product.slug}.{ext}"
        filepath = os.path.join(src_dir, filename)
        if os.path.exists(filepath):
            product.image = filename
            product.save()
            print(f"{product.name}: {filename} -> OK (slug)")
            found = True
            break
    if found:
        continue
    # 2. Поиск по ключевым словам в названии
    for key, fname in KEYWORDS.items():
        if key in product.name.lower():
            filepath = os.path.join(src_dir, fname)
            if os.path.exists(filepath):
                product.image = fname
                product.save()
                print(f"{product.name}: {fname} -> OK (keyword)")
                found = True
                break
    if not found:
        print(f"{product.name}: файл не найден для слага {product.slug} и ключевых слов")

print("Готово! Все товары обновлены.") 