from .base import *

environment = os.getenv('DJANGO_SETTINGS_MODULE', 'local')

if environment.endswith('production'):
    from .production import *
else:
    from .local import *