"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

import sys

# assuming your Django settings file is at '/home/fsclimentWagtail/wagtail/mysite/settings/production.py '

path = '/home/fsclimentWagtail/wagtail'

if path not in sys.path:

    sys.path.insert(0,path)

    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings.production'

## Uncomment the lines below depending on your Django version

###### then, for Django >=1.5:

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
