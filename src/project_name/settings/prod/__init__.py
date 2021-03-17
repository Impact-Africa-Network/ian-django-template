from ..base import *

DEBUG = False

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_REFERRER_POLICY = [
    "origin",
    "origin-when-cross-origin",
]

# SECURE_HSTS_SECONDS = 30

SECURE_HSTS_PRELOAD = True

SECURE_HSTS_INCLUDE_SUBDOMAINS = True
