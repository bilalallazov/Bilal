from django.core.management.base import BaseCommand
from store.models import Category, Product
from django.utils.text import slugify
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Добавляет тестовые данные в базу данных'

    def handle(self, *args, **kwargs):
        # Удаляем существующие данные
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создаем категории
        categories = {
            'engine': Category.objects.create(name='Двигатель', slug='engine'),
            'brake': Category.objects.create(name='Тормозная система', slug='brake-system'),
            'suspension': Category.objects.create(name='Подвеска', slug='suspension'),
            'body': Category.objects.create(name='Кузовные детали', slug='body-parts'),
            'electrical': Category.objects.create(name='Электрика', slug='electrical')
        }

        # Создаем товары с изображениями
        products = [
            {
                'category': categories['engine'],
                'name': 'Масляный фильтр Bosch',
                'description': 'Высококачественный масляный фильтр для всех типов двигателей',
                'price': 450,
                'stock': 100,
                'image': 'картинки/oil_filter.jpg'
            },
            {
                'category': categories['engine'],
                'name': 'Воздушный фильтр Mann',
                'description': 'Воздушный фильтр с увеличенным ресурсом',
                'price': 800,
                'stock': 50,
                'image': 'картинки/air_filter.jpg'
            },
            {
                'category': categories['brake'],
                'name': 'Тормозные колодки Brembo',
                'description': 'Передние тормозные колодки с высоким коэффициентом трения',
                'price': 2500,
                'stock': 30,
                'image': 'картинки/brake_pads.jpg'
            },
            {
                'category': categories['brake'],
                'name': 'Тормозной диск ATE',
                'description': 'Вентилируемый тормозной диск с защитным покрытием',
                'price': 3500,
                'stock': 20,
                'image': 'картинки/brake_disc.jpg'
            },
            {
                'category': categories['suspension'],
                'name': 'Амортизатор KYB',
                'description': 'Газонаполненный амортизатор для комфортной езды',
                'price': 4000,
                'stock': 15,
                'image': 'картинки/shock_absorber.jpg'
            },
            {
                'category': categories['suspension'],
                'name': 'Пружина подвески Sachs',
                'description': 'Пружина подвески с увеличенным ресурсом',
                'price': 2800,
                'stock': 25,
                'image': 'картинки/spring.jpg'
            },
            {
                'category': categories['body'],
                'name': 'Бампер передний',
                'description': 'Передний бампер из ударопрочного пластика',
                'price': 12000,
                'stock': 10,
                'image': 'картинки/bumper1.webp'
            },
            {
                'category': categories['body'],
                'name': 'Фара головного света',
                'description': 'LED фара головного света с дневными ходовыми огнями',
                'price': 15000,
                'stock': 8,
                'image': 'картинки/headlight.jpg'
            },
            {
                'category': categories['electrical'],
                'name': 'Аккумулятор Varta',
                'description': 'Аккумулятор с увеличенным сроком службы',
                'price': 8000,
                'stock': 20,
                'image': 'картинки/battery.jpg'
            },
            {
                'category': categories['electrical'],
                'name': 'Генератор Bosch',
                'description': 'Генератор с повышенной мощностью',
                'price': 25000,
                'stock': 5,
                'image': 'картинки/generator.jpg'
            }
        ]

        # Создаем тестовые изображения
        test_images = {
            'oil_filter.jpg': 'https://example.com/oil_filter.jpg',
            'air_filter.jpg': 'https://example.com/air_filter.jpg',
            'brake_pads.jpg': 'https://example.com/brake_pads.jpg',
            'brake_disc.jpg': 'https://example.com/brake_disc.jpg',
            'shock_absorber.jpg': 'https://example.com/shock_absorber.jpg',
            'spring.jpg': 'https://example.com/spring.jpg',
            'bumper1.webp': 'https://example.com/bumper1.webp',
            'headlight.jpg': 'https://example.com/headlight.jpg',
            'battery.jpg': 'https://example.com/battery.jpg',
            'generator.jpg': 'https://example.com/generator.jpg'
        }

        # Создаем пустые изображения для тестирования
        for image_name in test_images.keys():
            image_path = os.path.join(settings.MEDIA_ROOT, 'картинки', image_name)
            if not os.path.exists(image_path):
                with open(image_path, 'w') as f:
                    f.write('')

        # Создаем товары
        for product_data in products:
            Product.objects.create(
                category=product_data['category'],
                name=product_data['name'],
                slug=slugify(product_data['name']),
                description=product_data['description'],
                price=product_data['price'],
                stock=product_data['stock'],
                available=True,
                image=product_data['image']
            )

        self.stdout.write(self.style.SUCCESS('Тестовые данные успешно добавлены')) 