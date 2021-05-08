from .base import *
from __future__ import absolute_import, unicode_literals

import os

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
