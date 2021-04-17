from decouple import config

AWS_ACCESS_KEY_ID = config("SPACES_ACCESS_KEY")

AWS_SECRET_ACCESS_KEY = config("SPACES_SECRET_KEY")

AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")

AWS_S3_ENDPOINT_URL = "https://nyc3.digitaloceanspaces.com"

AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}

AWS_LOCATION = "static"

AWS_STATIC_LOCATION = f"{AWS_LOCATION}/static"

AWS_S3_SIGNATURE_VERSION = "s3"  # DigitalOcean supports only v2

AWS_DEFAULT_ACL = "public-read"

DEFAULT_FILE_STORAGE = "{{project_name}}.settings.dgo.utils.MediaRootS3BotoStorage"

STATICFILES_STORAGE = "{{project_name}}.settings.dgo.utils.StaticRootS3BotoStorage"

STATIC_URL = "{}/{}/".format(AWS_S3_ENDPOINT_URL, AWS_STATIC_LOCATION)

AWS_PUBLIC_MEDIA_LOCATION = f"{AWS_LOCATION}/media/public"

AWS_PRIVATE_MEDIA_LOCATION = f"{AWS_LOCATION}/media/private"

PRIVATE_FILE_STORAGE = "{{project_name}}.settings.dgo.utils.MediaRootS3BotoStorage"

STATIC_ROOT = "static/"
