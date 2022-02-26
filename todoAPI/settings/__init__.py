from __future__ import absolute_import
from .base import *

environment = os.getenv('DJANGO_SETTINGS_MODULE')
print(environment)
from .pxasd import *

# if environment.endswith('production'):
# else:
    # from todoAPI.settings.local import *