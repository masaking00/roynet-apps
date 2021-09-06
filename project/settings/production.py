from .base import *

DEBUG = False

ALLOWED_HOSTS = ['118.27.16.78']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myblog',
        'USER': 'root',
        'PASSWPRD': '123456789',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}