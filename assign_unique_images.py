import os
import django

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carstore.settings')
    django.setup()
    from store.models import Product

    mapping = {
        'Бампер передний': 'product-38.webp',
        'Пружина подвески Sachs': 'spring_suspension.webp',
        'Тормозной диск ATE': 'brake_discs.webp',
        'Тормозные колодки Brembo': 'kyb.webp',
        'Амортизатор KYB': 'i (6).webp',
        'Воздушный фильтр Mann': 'vozduh.jpg',
        'Масляный фильтр Bosch': 'sachs.webp',
    }

    products = Product.objects.all()
    for product in products:
        filename = mapping.get(product.name)
        if filename:
            product.image.name = f'products/{filename}'
            product.save()
            print(f'{product.name} -> {filename}')
        else:
            print(f'{product.name} -> (оставлено без изменений)')

if __name__ == "__main__":
    main() 