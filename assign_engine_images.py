import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carstore.settings')
django.setup()

from store.models import Product, Category

# Соответствие: название товара -> имя файла картинки
images = {
    'Вал коленчатый': 'val_kolenchatyy.webp',
    'Головка блока цилиндров': 'golovka_bloka.webp',
    'Ремень ГРМ': 'remengrm.webp',
    'Ролик ГРМ': 'rolikgrm.webp',
    'Ремень генератора': 'remen_generatora.webp',
    'Натяжной ролик': 'natjazhnoi_rolik.webp',
    'Гидрокомпенсатор': 'gazoraspr.webp',
    'Система смазки двигателя': 'smazka_dvigatelya.webp',
    'Шатун': 'shatun.webp',
    'Поршень': 'porshen.webp',
    'Кольца поршневые': 'kolca_porshnevye.webp',
    'Шкив': 'shkiv.webp',
}

for name, filename in images.items():
    p = Product.objects.filter(name=name).first()
    if p:
        p.image = f'картинки/{filename}'
        p.save()
        print(f'Установлено изображение для: {name} -> {filename}')
    else:
        print(f'Товар не найден: {name}') 