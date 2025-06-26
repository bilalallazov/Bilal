from django.core.management.base import BaseCommand
from store.models import Product, Cart, CartItem
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Добавляет первые 5 товаров в корзину первого пользователя'

    def handle(self, *args, **kwargs):
        user = User.objects.first()
        if not user:
            self.stdout.write(self.style.ERROR('Нет пользователей в базе данных!'))
            return
        cart, _ = Cart.objects.get_or_create(user=user)
        products = Product.objects.all()[:5]
        for product in products:
            item, created = CartItem.objects.get_or_create(cart=cart, product=product, defaults={'quantity': 1})
            if not created:
                item.quantity = 1
                item.save()
            self.stdout.write(self.style.SUCCESS(f'Добавлен товар: {product.name}'))
        self.stdout.write(self.style.SUCCESS('Корзина заполнена!'))

        # Меняем картинку у товара 'Воздушный фильтр'
        p = Product.objects.filter(name__icontains='Воздушный фильтр').first()
        if p:
            p.image = 'картинки/аккумулятор.webp'
            p.save()
            self.stdout.write(self.style.SUCCESS('Картинка для "Воздушный фильтр" изменена на аккумулятор.webp'))
        else:
            self.stdout.write(self.style.ERROR('Товар "Воздушный фильтр" не найден!')) 