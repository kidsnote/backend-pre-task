import os

from .base import *


DEBUG = True

SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-4h(4(tkle+h!x*81b(r9!!z4jous7ld3!nwfx7ra^w39!z2vls",
)
