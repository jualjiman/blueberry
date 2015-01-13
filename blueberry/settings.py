"""
Django settings for blueberry project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yn=oy%(3+5@v*3i%*is8995$t1nobfcc#&erx@d3+=g1!uc_nv'

# SECURITY WARNING: don't run with debug turned on in production!
debugsm = False
DEBUG = debugsm
TEMPLATE_DEBUG = debugsm

ALLOWED_HOSTS = ['.edecanesenacapulco.com.mx','.edecanesenacapulco.com.mx.']
#ALLOWED_HOSTS = ['.bb.jualjiman.com','.bb.jualjiman.com.']
#ALLOWED_HOSTS = []

# Application definition


from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

#GRAPPELLI_ADMIN_TITLE = "Blueberry | Agencia de edecanes"

INSTALLED_APPS = (
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'administrador',
    'sorl.thumbnail',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'blueberry.urls'

WSGI_APPLICATION = 'blueberry.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""

DATABASES = {
    'default': {
        'NAME': 'blueberry',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'wadmin',
        'PASSWORD': '081510979s'
    }
  }

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_CHARSET = 'utf-8'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'administrador/static')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

ADMIN_MEDIA_PREFIX = '/static/admin/'

MEDIA_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['media'])
MEDIA_URL = '/media/'
