# АвтоЗапчасти - Интернет-магазин автозапчастей

Интернет-магазин автозапчастей, разработанный на Django.

## Функциональность

- Каталог автозапчастей с категориями
- Поиск по каталогу
- Корзина покупок
- Система аутентификации
- Личный кабинет пользователя
- Админ-панель для управления товарами

## Установка

1. Клонируйте репозиторий
2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
```
3. Установите зависимости:
```bash
pip install -r requirements.txt
```
4. Примените миграции:
```bash
python manage.py migrate
```
5. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```
6. Запустите сервер:
```bash
python manage.py runserver
```

## Технологии

- Django 5.0.2
- Bootstrap 5
- SQLite (для разработки)
- Pillow для работы с изображениями
- django-crispy-forms для форм
- django-allauth для аутентификации 