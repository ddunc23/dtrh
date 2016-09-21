from .secret_settings import *
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

STATICFILES_DIRS = [
    BASE_DIR.child('static'),
    'static/',
]