from setuptools import setup

setup(
    name="bilal_project",
    version="0.1.0",
    install_requires=[
        "Django==5.0.2",
        "gunicorn",
        "dj-database-url",
        "whitenoise",
        "Pillow==10.2.0"
    ],
) 