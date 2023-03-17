"""
ASGI config for promocap project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from dj_static import MediaCling, Cling
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'promocap.settings')

application = Cling(MediaCling(get_asgi_application()))
