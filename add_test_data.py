from store.models import Category, Product
from django.utils.text import slugify

# Создаем категории
categories_data = [
    {
        'name': 'Двигатель',
        'slug': 'engine',
    },
    {
        'name': 'Тормозная система',
        'slug': 'brake-system',
    },
    {
        'name': 'Подвеска',
        'slug': 'suspension',
    },
    {
        'name': 'Кузовные детали',
        'slug': 'body-parts',
    },
    {
        'name': 'Электрика',
        'slug': 'electrical',
    }
]

# Создаем товары
products_data = [
    {
        'category': 'Двигатель',
        'name': 'Масляный фильтр Bosch',
        'description': 'Высококачественный масляный фильтр для всех типов двигателей',
        'price': 450,
        'stock': 100,
        'available': True,
    },
    {
        'category': 'Двигатель',
        'name': 'Воздушный фильтр Mann',
        'description': 'Воздушный фильтр с увеличенным ресурсом',
        'price': 800,
        'stock': 50,
        'available': True,
    },
    {
        'category': 'Тормозная система',
        'name': 'Тормозные колодки Brembo',
        'description': 'Передние тормозные колодки с высоким коэффициентом трения',
        'price': 2500,
        'stock': 30,
        'available': True,
    },
    {
        'category': 'Тормозная система',
        'name': 'Тормозной диск ATE',
        'description': 'Вентилируемый тормозной диск с защитным покрытием',
        'price': 3500,
        'stock': 20,
        'available': True,
    },
    {
        'category': 'Подвеска',
        'name': 'Амортизатор KYB',
        'description': 'Газонаполненный амортизатор для комфортной езды',
        'price': 4000,
        'stock': 15,
        'available': True,
    },
    {
        'category': 'Подвеска',
        'name': 'Пружина подвески Sachs',
        'description': 'Пружина подвески с увеличенным ресурсом',
        'price': 2800,
        'stock': 25,
        'available': True,
    },
    {
        'category': 'Кузовные детали',
        'name': 'Бампер передний',
        'description': 'Передний бампер из ударопрочного пластика',
        'price': 12000,
        'stock': 10,
        'available': True,
    },
    {
        'category': 'Кузовные детали',
        'name': 'Фара головного света',
        'description': 'LED фара головного света с дневными ходовыми огнями',
        'price': 15000,
        'stock': 8,
        'available': True,
    },
    {
        'category': 'Электрика',
        'name': 'Аккумулятор Varta',
        'description': 'Аккумулятор с увеличенным сроком службы',
        'price': 8000,
        'stock': 20,
        'available': True,
    },
    {
        'category': 'Электрика',
        'name': 'Генератор Bosch',
        'description': 'Генератор с повышенной мощностью',
        'price': 25000,
        'stock': 5,
        'available': True,
    }
]

# Создаем категории
for cat_data in categories_data:
    Category.objects.get_or_create(
        name=cat_data['name'],
        slug=cat_data['slug']
    )

# Создаем товары
for prod_data in products_data:
    category = Category.objects.get(name=prod_data['category'])
    Product.objects.get_or_create(
        category=category,
        name=prod_data['name'],
        slug=slugify(prod_data['name']),
        description=prod_data['description'],
        price=prod_data['price'],
        stock=prod_data['stock'],
        available=prod_data['available']
    ) 