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
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD' : os.getenv('DB_PASSWORD'),
        'HOST' : os.getenv('DB_HOST'),
        'PORT' : os.getenv('DB_PORT'),
    }
}

