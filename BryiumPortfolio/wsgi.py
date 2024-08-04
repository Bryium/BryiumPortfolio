"""
WSGI config for BryiumPortfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

from BryiumPortfolio.settings import BASE_DIR

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BryiumPortfolio.settings')

application = get_wsgi_application()

app = application

from whitenoise import WhiteNoise
from BryiumPorfolio import MyWSGIApp

application = MyWSGIApp()
application = WhiteNoise(application, root=str(BASE_DIR / 'staticfiles'))
application.add_files(str(BASE_DIR / 'Home/static'), prefix='static/')
