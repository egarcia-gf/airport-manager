import os

environment = os.getenv('DJANGO_ENV', 'desarrollo')

if environment == 'produccion':
    from .produccion import *
elif environment == 'staging':
    from .staging import *
else:
    from .desarrollo import *