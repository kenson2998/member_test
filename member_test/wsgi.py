# mysite/mysite/wsgi.py

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "appkenson.settings")

# application = Cling(get_wsgi_application())

# from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "member_test.settings")
application = get_wsgi_application()
application = DjangoWhiteNoise(application)