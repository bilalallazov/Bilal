from django.core.management.base import BaseCommand
from store.models import Category
from django.core.files import File
import os

CATEGORY_IMAGES = {
    'Двигатель': 'engine.jpg',
    'Кузовные детали': 'bumper.jpg',
    'Подвеска': 'shock_absorber.jpg',
    'Тормозная система': 'brake_pads.jpg',
    'Электрика': 'headlight.jpg',
}

class Command(BaseCommand):
    help = 'Автоматически добавляет изображения к основным категориям.'

    def handle(self, *args, **options):
        # Путь к папке картинки внутри проекта
        base_dir = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.dirname(os.path.abspath(__file__))
                    )
                )
            ),
            'картинки'
        )
        updated = 0
        for cat_name, img_name in CATEGORY_IMAGES.items():
            # Для двигателя ищем подходящее изображение
            if cat_name == 'Двигатель':
                candidates = ['engine.jpg', 'orig.png', 'battery.jpg']
                for candidate in candidates:
                    img_path = os.path.join(base_dir, candidate)
                    if os.path.exists(img_path):
                        img_name = candidate
                        break
            else:
                img_path = os.path.join(base_dir, img_name)
            try:
                category = Category.objects.get(name=cat_name)
                if os.path.exists(img_path):
                    with open(img_path, 'rb') as f:
                        category.image.save(img_name, File(f), save=True)
                    self.stdout.write(self.style.SUCCESS(f'Изображение для "{cat_name}" успешно добавлено.'))
                    updated += 1
                else:
                    self.stdout.write(self.style.WARNING(f'Файл {img_path} не найден.'))
            except Category.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Категория "{cat_name}" не найдена.'))
        if updated:
            self.stdout.write(self.style.SUCCESS(f'Обновлено {updated} категорий.'))
        else:
            self.stdout.write(self.style.WARNING('Ни одна категория не была обновлена.')) 