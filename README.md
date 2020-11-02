# BMI

Explicitamente esta documentación será en español y contendrá lo siguiente.

  - Requisitos
  - Como ejecutar el software local
  - Descripciones principales
  
# Requisitos

  - Python 3.8
  - Pipenv (para la gestión de entornos virtuales) https://pipenv-es.readthedocs.io/es/latest/install.html
  - Sqlite (elegida por simpleza para correr en local) https://www.sqlite.org/index.html


# Como ejecutar el software local
copiar dentro de la carpeta BMI
```sh
$ cd BMI
$ pipenv --three
$ pipenv install
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

Esto ejecutará el software en local y en el puerto 8000.

```sh
http://127.0.0.1:8000
```

Para mas información: https://docs.djangoproject.com/en/3.1/ref/django-admin/#runserver

# Descripciones principales


