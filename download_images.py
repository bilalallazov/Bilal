import os
import urllib.request

IMAGES = {
    'oil_filter.jpg': 'https://i.ibb.co/VqG8LzX/oil-filter.jpg',
    'air_filter.jpg': 'https://i.ibb.co/0jZ8LzX/air-filter.jpg',
    'brake_pads.jpg': 'https://i.ibb.co/0jZ8LzX/brake-pads.jpg',
    'brake_disc.jpg': 'https://i.ibb.co/0jZ8LzX/brake-disc.jpg',
    'shock_absorber.jpg': 'https://i.ibb.co/0jZ8LzX/shock-absorber.jpg',
    'spring.jpg': 'https://i.ibb.co/0jZ8LzX/spring.jpg',
    'bumper1.webp': 'https://i.ibb.co/0jZ8LzX/bumper.jpg',
    'headlight.jpg': 'https://i.ibb.co/0jZ8LzX/headlight.jpg',
    'battery.jpg': 'https://i.ibb.co/0jZ8LzX/battery.jpg',
    'generator.jpg': 'https://i.ibb.co/0jZ8LzX/generator.jpg',
}

def main():
    os.makedirs('картинки', exist_ok=True)
    for filename, url in IMAGES.items():
        path = os.path.join('картинки', filename)
        print(f'Скачиваю {filename}...')
        try:
            urllib.request.urlretrieve(url, path)
            print(f'  -> {filename} успешно загружен')
        except Exception as e:
            print(f'  -> Ошибка при загрузке {filename}: {e}')

if __name__ == '__main__':
    main() 