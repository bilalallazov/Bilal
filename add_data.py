from store.models import Category, Product
from django.utils.text import slugify

# Создаем категории
Category.objects.create(name='Двигатель', slug='engine')
Category.objects.create(name='Тормозная система', slug='brake-system')
Category.objects.create(name='Подвеска', slug='suspension')
Category.objects.create(name='Кузовные детали', slug='body-parts')
Category.objects.create(name='Электрика', slug='electrical')

# Получаем категории
engine = Category.objects.get(name='Двигатель')
brake = Category.objects.get(name='Тормозная система')
suspension = Category.objects.get(name='Подвеска')
body = Category.objects.get(name='Кузовные детали')
electrical = Category.objects.get(name='Электрика')

# Создаем товары
Product.objects.create(
    category=engine,
    name='Масляный фильтр Bosch',
    slug='maslyanyy-filtr-bosch',
    description='Высококачественный масляный фильтр для всех типов двигателей',
    price=450,
    stock=100,
    available=True
)

Product.objects.create(
    category=engine,
    name='Воздушный фильтр Mann',
    slug='vozdushnyy-filtr-mann',
    description='Воздушный фильтр с увеличенным ресурсом',
    price=800,
    stock=50,
    available=True
)

Product.objects.create(
    category=brake,
    name='Тормозные колодки Brembo',
    slug='tormoznye-kolodki-brembo',
    description='Передние тормозные колодки с высоким коэффициентом трения',
    price=2500,
    stock=30,
    available=True
)

Product.objects.create(
    category=brake,
    name='Тормозной диск ATE',
    slug='tormoznoy-disk-ate',
    description='Вентилируемый тормозной диск с защитным покрытием',
    price=3500,
    stock=20,
    available=True
)

Product.objects.create(
    category=suspension,
    name='Амортизатор KYB',
    slug='amortizator-kyb',
    description='Газонаполненный амортизатор для комфортной езды',
    price=4000,
    stock=15,
    available=True
)

Product.objects.create(
    category=suspension,
    name='Пружина подвески Sachs',
    slug='pruzhina-podveski-sachs',
    description='Пружина подвески с увеличенным ресурсом',
    price=2800,
    stock=25,
    available=True
)

Product.objects.create(
    category=body,
    name='Бампер передний',
    slug='bamper-peredniy',
    description='Передний бампер из ударопрочного пластика',
    price=12000,
    stock=10,
    available=True
)

Product.objects.create(
    category=body,
    name='Фара головного света',
    slug='fara-golovnogo-sveta',
    description='LED фара головного света с дневными ходовыми огнями',
    price=15000,
    stock=8,
    available=True
)

Product.objects.create(
    category=electrical,
    name='Аккумулятор Varta',
    slug='akkumulyator-varta',
    description='Аккумулятор с увеличенным сроком службы',
    price=8000,
    stock=20,
    available=True
)

Product.objects.create(
    category=electrical,
    name='Генератор Bosch',
    slug='generator-bosch',
    description='Генератор с повышенной мощностью',
    price=25000,
    stock=5,
    available=True
) 