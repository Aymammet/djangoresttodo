
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "todo", 
        'USER': 'postgres',
        'PASSWORD' : 'postgres',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}



