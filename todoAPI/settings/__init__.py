from __future__ import absolute_import
from .base import *

environment = os.getenv('DJANGO_SETTINGS_MODULE', 'local')
print(environment)
if environment.endswith('production'):
    from todoAPI.settings.production import *
else:
    from todoAPI.settings.local import *