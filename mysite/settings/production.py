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


DEBUG = int(env['DEBUG'])

try:
    from .local import *
except ImportError:
    pass

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE'),
        'NAME': os.environ.get('DB_DATABASE_NAME', os.path.join(BASE_DIR)),
        'USER': os.environ.get('DB_USERNAME'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}
	
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env['EMAIL_HOST']
EMAIL_PORT = env['EMAIL_PORT']