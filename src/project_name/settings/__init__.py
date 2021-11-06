from .base import *
from decouple import config

DEBUG = config("DEBUG", False, cast=bool)

ENVIRONMENT = config("ENVIRONMENT", "AWS")

if ENVIRONMENT == "DGO":
    from .dgo import *
if ENVIRONMENT == "AWS":
    from .aws import *
if ENVIRONMENT == "GCP":
    from .gcp import *

if DEBUG:
    from .dev import *
else:
    from .prod import *

# STATIC_ROOT = os.path.join(BASE_DIR, "static")