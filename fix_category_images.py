import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carstore.settings')
import django
django.setup()
from store.models import Category

updated = 0
for cat in Category.objects.all():
    if cat.image and cat.image.name.startswith('картинки/картинки/'):
        cat.image.name = cat.image.name.replace('картинки/картинки/', 'картинки/')
        cat.save()
        updated += 1
print(f'Updated {updated} categories.') 