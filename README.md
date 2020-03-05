# Django Test

Simple toy skeleton of a Django project for playing around with Django.

It's sort of a simple rest api over a single resource of a basic counter
object.

## Getting Started

Create a Python virtual environment and install the dependencies:

```shell
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

Then make sure you export your `DJANGO_SETTINGS_MODULE` environment variable:

```shell
export DJANGO_SETTINGS_MODULE=djangotest.settings
```

## Running The Tests

```shell
python manage.py test djangotest
```
