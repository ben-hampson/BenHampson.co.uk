# Parse database configuration from $DATABASE_URL
from __future__ import absolute_import, unicode_literals
import dj_database_url
from .base import *

import os

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

AWS_ACCESS_KEY_ID = env['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = env['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = env['AWS_STORAGE_BUCKET_NAME']
AWS_S3_FILE_OVERWRITE = False  # If someone uploads a file with a name that's the same as an existing file, don't overwrite
AWS_DEFAULT_ACL = None  # The file will inherit the bucket's permission
AWS_S3_REGION_NAME = "eu-west-2"
AWS_S3_ADDRESSING_STYLE = 'virtual'
AWS_S3_SIGNATURE_VERSION = "s3v4"

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


DEBUG = True

try:
    from .local import *
except ImportError:
    pass

DATABASES = {
    'default': dj_database_url.config()
}
	
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']