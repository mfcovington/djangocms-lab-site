from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(3i0+39s*@2=p3tjdopjb=v45ay3_dm0ej47(d_9)o82-7@5zm'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'PORT': '',
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'project.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost'
    }
}
