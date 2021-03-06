#!/usr/bin/env python3
"""
WSGI config for ptweb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append('/var/www/pythonankara_com/ptweb/')
sys.path.append('/var/www/pythonankara_com/ptweb/ptweb')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ptweb.settings")

application = get_wsgi_application()
