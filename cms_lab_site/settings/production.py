from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('MALOOF_LAB_SECRET_KEY', '')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = DEBUG


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'maloof_lab_site_db',
        'USER': 'maloof_lab_site_admin',
        # password will passed from environmental variable:
        'PASSWORD': os.environ.get('MALOOF_LAB_SITE_DB_PASSWORD', ''),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# CHANGE DEPENDING ON HOST
ALLOWED_HOSTS = ['symposium.plb.ucdavis.edu']


# Application definition
WSGI_APPLICATION = 'cms_lab_site.wsgi.application'
