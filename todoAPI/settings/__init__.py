from todoAPI.settings.base import *

environment = os.getenv('DJANGO_SETTINGS_MODULE', 'local')

# from todoAPI.settings.local import *

if environment.endswith('production'):
    from todoAPI.settings.production import *
else:
    from todoAPI.settings.base import *