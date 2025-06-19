from PIL import Image, ImageDraw, ImageFont
import os
from store.models import Product
from django.conf import settings

MEDIA_PATH = os.path.join(settings.BASE_DIR, 'media', 'products')

def create_part_image(filename, text, color):
    # Создаем изображение
    img = Image.new('RGB', (400, 400), color='white')
    draw = ImageDraw.Draw(img)
    
    # Рисуем рамку
    draw.rectangle([(10, 10), (390, 390)], outline='black', width=2)
    
    # Добавляем текст
    try:
        font = ImageFont.truetype("arial.ttf", 36)
    except:
        font = ImageFont.load_default()
    
    # Центрируем текст
    text_width = draw.textlength(text, font=font)
    text_position = ((400 - text_width) // 2, 180)
    
    draw.text(text_position, text, fill='black', font=font)
    
    # Сохраняем изображение
    os.makedirs('картинки', exist_ok=True)
    img.save(os.path.join('картинки', filename))

# Создаем изображения для каждой запчасти
parts = [
    ('oil_filter.jpg', 'Масляный фильтр', '#FFE4E1'),
    ('air_filter.jpg', 'Воздушный фильтр', '#E0FFFF'),
    ('brake_pads.jpg', 'Тормозные колодки', '#F0FFF0'),
    ('brake_pads.jpg', 'Тормозной диск', '#FFF0F5'),
    ('shock_absorber.jpg', 'Амортизатор', '#F5F5DC'),
    ('spring.jpg', 'Пружина подвески', '#F0F8FF'),
    ('bumper.jpg', 'Бампер', '#FFFAFA'),
    ('headlight.jpg', 'Фара', '#F8F8FF'),
    ('battery.jpg', 'Аккумулятор', '#F5F5F5'),
    ('generator.jpg', 'Генератор', '#FAFAD2'),
]

for filename, text, color in parts:
    create_part_image(filename, text, color)
    print(f'Создано изображение: {filename}')

count = 0
for product in Product.objects.all():
    slug = product.slug
    for ext in ['jpg', 'jpeg', 'png']:
        filename = f"{slug}.{ext}"
        filepath = os.path.join(MEDIA_PATH, filename)
        if os.path.exists(filepath):
            product.image = f"products/{filename}"
            product.save()
            print(f"Картинка для {product.name} установлена: {filename}")
            count += 1
            break
print(f"Всего обновлено товаров: {count}") 