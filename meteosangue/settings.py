"""
Django settings for meteosangue project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os, sys

VERSION = '1.1.0'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SECRET_KEY = os.getenv('SECRET_KEY', 'S3KR3TK3Y_D3V')

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN', 'D3V')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET', 'D3V')
CONSUMER_KEY = os.getenv('CONSUMER_KEY', 'D3V')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET', 'D3V')

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', 'D3V')
TELEGRAM_CHANNEL = os.getenv('TELEGRAM_CHANNEL', 'D3V')

FACEBOOK_TOKEN = os.getenv('FACEBOOK_TOKEN', 'D3V')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'api',
    'django_rq',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'meteosangue.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'meteosangue.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'meteosangue.sqlite3'),
        },
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'USER': 'astagi',
            'NAME': 'meteosangue',
            'TEST': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'meteosangue.sqlite3'),
            },
        },
    }


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Blood associations data

BLOOD_ASSOCIATIONS = [

    {
        'name': 'Avis Nazionale',
        'twitter_id': '@avisnazionale',
        'facebook_id': ''
    },

    {
        'name': 'Avis Giovani',
        'twitter_id': '@giovaniavis',
        'facebook_id': ''
    },

    {
        'name': 'Fidas Nazionale',
        'twitter_id': '@FIDASnazionale',
        'facebook_id': ''
    },

    {
        'name': 'Frates Nazionale',
        'twitter_id': '@FratresNaz',
        'facebook_id': ''
    },

    {
        'name': 'Centro Naz. Sangue',
        'twitter_id': '@CentroSangue',
        'facebook_id': ''
    }

]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

ENV_PATH = os.path.abspath(os.path.dirname(__file__))
UPLOAD_ROOT = os.path.join(ENV_PATH, 'uploads/')
UPLOAD_METEO = os.path.join(UPLOAD_ROOT, 'meteo/')

BLOOD_FETCH_INTERVAL = 60 * 15

RQ_QUEUES = {
    'default': {
        'URL': os.getenv('REDIS_URL', 'redis://localhost:6379/0'),
        'DEFAULT_TIMEOUT': 60 * 20,
    },
    'high': {
        'URL': os.getenv('REDIS_URL', 'redis://localhost:6379/0'),
        'DEFAULT_TIMEOUT': 60 * 20,
    },
    'low': {
        'URL': os.getenv('REDIS_URL', 'redis://localhost:6379/0'),
        'DEFAULT_TIMEOUT': 60 * 20,
    }
}

import dj_database_url
db_from_env = dj_database_url.config()
if db_from_env:
    DATABASES['default'].update(db_from_env)

if 'test' in sys.argv:
    try:
        from .test_settings import *
    except ImportError:
        pass
else:
    try:
        from .local_settings import *
    except ImportError:
        pass
