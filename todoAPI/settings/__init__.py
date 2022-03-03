from todoAPI.settings.base import *
url = "127.0.0.1"

environment = os.getenv('DJANGO_SETTINGS_MODULE', 'local')

if environment.endswith('production'):
    from todoAPI.settings.production import *
    url = "https://todo-aymammet.herokuapp.com"
