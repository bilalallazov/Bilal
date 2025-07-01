import os
import django

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carstore.settings')
    django.setup()
    from store.models import Product

    mapping = {'картинки/bumper.jpg': 'products/bumper1.webp'}
    updated = 0
    products = Product.objects.all()
    for p in products:
        if p.image.name and not p.image.name.startswith('products/'):
            new_name = mapping.get(p.image.name, f'products/{os.path.basename(p.image.name)}')
            p.image.name = new_name
            p.save()
            print(f"Updated: {p.name} -> {new_name}")
            updated += 1
    print(f"Всего обновлено: {updated}")

if __name__ == "__main__":
    main() 