from django.core.management.base import BaseCommand
from store.models import Product

class Command(BaseCommand):
    help = 'Исправляет названия товаров'

    def handle(self, *args, **kwargs):
        # Исправление аккумулятора
        product = Product.objects.filter(name__iexact='ккумулятор').first()
        if product:
            product.name = 'Аккумулятор'
            product.save()
            self.stdout.write(self.style.SUCCESS('Название исправлено на Аккумулятор'))
        else:
            self.stdout.write(self.style.ERROR('Товар с именем "ккумулятор" не найден!'))
        # Исправление амортизатора
        product2 = Product.objects.filter(name__iexact='Амортизатор KYB').first()
        if product2:
            product2.name = 'Амортизатор'
            product2.save()
            self.stdout.write(self.style.SUCCESS('Название исправлено на Амортизатор'))
        else:
            self.stdout.write(self.style.ERROR('Товар с именем "Амортизатор KYB" не найден!'))
        # Исправление генератора
        product3 = Product.objects.filter(name__iexact='Генератор Bosch').first()
        if product3:
            product3.name = 'Генератор'
            product3.save()
            self.stdout.write(self.style.SUCCESS('Название исправлено на Генератор'))
        else:
            self.stdout.write(self.style.ERROR('Товар с именем "Генератор Bosch" не найден!'))
        # Исправление пружины подвески
        product4 = Product.objects.filter(name__iexact='Пружина подвески Sachs').first()
        if product4:
            product4.name = 'Пружина подвески'
            product4.save()
            self.stdout.write(self.style.SUCCESS('Название исправлено на Пружина подвески'))
        else:
            self.stdout.write(self.style.ERROR('Товар с именем "Пружина подвески Sachs" не найден!'))
        # Исправление тормозного диска
        product5 = Product.objects.filter(name__iexact='Тормозной диск ATE').first()
        if product5:
            product5.name = 'Тормозной диск'
            product5.save()
            self.stdout.write(self.style.SUCCESS('Название исправлено на Тормозной диск'))
        else:
            self.stdout.write(self.style.ERROR('Товар с именем "Тормозной диск ATE" не найден!'))
        # Исправление тормозных колодок
        product6 = Product.objects.filter(name__iexact='Тормозные колодки Brembo').first()
        if product6:
            product6.name = 'Тормозные колодки'
            product6.save()
            self.stdout.write(self.style.SUCCESS('Название исправлено на Тормозные колодки'))
        else:
            self.stdout.write(self.style.ERROR('Товар с именем "Тормозные колодки Brembo" не найден!')) 