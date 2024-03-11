from .base_settings import *
import sys


SESSION_COOKIE_AGE = 1 * 10


if 'test' in sys.argv:
    DATABASES['default'] = DATABASES['test']
