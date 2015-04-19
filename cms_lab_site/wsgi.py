"""
WSGI config for cms_lab_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

from django.core.handlers.wsgi import WSGIHandler
import django
import os

class WSGIEnvironment(WSGIHandler):

    def __call__(self, environ, start_response):

        os.environ['MALOOF_LAB_SECRET_KEY'] = environ['MALOOF_LAB_SECRET_KEY']
        os.environ['MALOOF_LAB_SITE_DB_PASSWORD'] = environ['MALOOF_LAB_SITE_DB_PASSWORD']
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cms_lab_site.settings.production')
        django.setup()
        return super(WSGIEnvironment, self).__call__(environ, start_response)

application = WSGIEnvironment()
