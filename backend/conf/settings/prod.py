import os

from .base import *

DEBUG = False

SECRET_KEY = os.environ.get("SECRET_KEY")
ADMINS = [
    ("Lee Jong Seong", "dlwhdtjd098@gmail.com"),
]
