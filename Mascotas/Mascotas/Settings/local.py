from .base import *

DATABASES = {
    
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'infomascotas',
            'USER': 'root',
            'PASSWORD': 'informatorio',
            'HOST': 'localhost',
            'PORT': '3306',

        }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
