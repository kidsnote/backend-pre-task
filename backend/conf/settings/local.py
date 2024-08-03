import os

from .base import *


DEBUG = True
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-4h(4(tkle+h!x*81b(r9!!z4jous7ld3!nwfx7ra^w39!z2vls",
)
MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]
INTERNAL_IPS = [
    "127.0.0.1",
]

# docker 에서 실행 시 internal ips가 동적으로 할당 되므로, 아래와 같이 설정해준다
import socket

hostname, _, ips = socket.gethostbyname_ex(
    socket.gethostname()
)
INTERNAL_IPS += [
    ".".join(ip.split(".")[:-1] + ["1"]) for ip in ips
]
