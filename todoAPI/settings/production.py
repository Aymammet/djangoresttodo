import os

# DEBUG = True

# ALLOWED_HOSTS = ['*']

# DATABASES = {
#    'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': "todo", 
#         'USER': 'postgres',
#         'PASSWORD' : 'postgres',
#         'HOST' : 'localhost',
#         'PORT' : '5432',
#     }
# }

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['https://todo-aymammet.herokuapp.com']

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

