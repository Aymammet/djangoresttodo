import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['https://todo-aymammet.herokuapp.com']

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "d8b0squa5j31ip",
        'USER': 'kgzpnadlhcyzrs',
        'PASSWORD' : '7dbe844a3fc740e3b3392e7dcd0165b2ebe1d13496291b0399293de8ead22c22',
        'HOST' : 'ec2-44-193-188-118.compute-1.amazonaws.com',
        'PORT' : '5432',
    }
}


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

