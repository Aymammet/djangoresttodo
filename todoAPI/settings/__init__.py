from __future__ import absolute_import
from .base import *

environment = os.getenv('DJANGO_SETTINGS_MODULE')
print(environment)
from .production import *

# if environment.endswith('production'):
# else:
    # from todoAPI.settings.local import *