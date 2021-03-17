from decouple import config

DEBUG = config("DEBUG", True, cast=bool)
