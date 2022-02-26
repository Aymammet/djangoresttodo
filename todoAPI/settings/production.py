import os

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('NAME'),
        'USER': os.getenv('USER'),
        'PASSWORD' : os.getenv('PASSWORD'),
        'HOST' : os.getenv('HOST'),
        'PORT' : os.getenv('PORT'),
    }
}

