import datetime

from decouple import config

AWS_DEFAULT_ACL = None
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False
AWS_AUTO_CREATE_BUCKET = True
DEFAULT_FILE_STORAGE = '{{project_name}}.settings.aws.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = '{{project_name}}.settings.aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
S3DIRECT_REGION = 'us-east-1'
S3_URL = f'//{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/' 
MEDIA_URL = f'//{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/media/' 
MEDIA_ROOT = MEDIA_URL
STATIC_URL = f'{S3_URL}static/'
ADMIN_MEDIA_PREFIX = f'{STATIC_URL}admin/'

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = {
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}
