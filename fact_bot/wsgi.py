"""
WSGI config for fact_bot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fact_bot_portal.settings")

application = get_wsgi_application()

from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)
