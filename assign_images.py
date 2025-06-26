import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carstore.settings')
django.setup()

import shutil
from store.models import Product
from django.conf import settings

src_dir = os.path.join(settings.BASE_DIR, 'картинки')
dst_dir = os.path.join(settings.BASE_DIR, 'media', 'products')
os.makedirs(dst_dir, exist_ok=True)

image_files = [f for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, f))]
image_files.sort()

for product, image_file in zip(Product.objects.all(), image_files):
    ext = os.path.splitext(image_file)[1].lower()
    new_filename = f"{product.slug}{ext}"
    src_path = os.path.join(src_dir, image_file)
    dst_path = os.path.join(dst_dir, new_filename)
    shutil.copyfile(src_path, dst_path)
    product.image = f"products/{new_filename}"
    product.save()
    print(f"{product.name}: {image_file} -> {new_filename}")

print("Готово! Картинки сопоставлены и переименованы.") 