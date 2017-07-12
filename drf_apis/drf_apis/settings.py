"""
Django settings for drf_apis project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from local_settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%ixj6r*@dd^&e&1#e!+5@-^11qi1wsyk0i-db18-%rnmo+w%r#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', 'fnii96lzya.execute-api.us-east-2.amazonaws.com','fnii96lzya.execute-api.us-east-2.amazonaws.com', '127.0.0.1', 'drfbaseball.ca40m5uvqobb.us-east-1.rds.amazonaws.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_extensions',
    'storages',
    'boto3',
    'zappa',
    'drf_apis.drf_baseball'
]
ZAPPA_SETTINGS = {
        'dev':
    {
            's3_bucket': 'zappa-baseball',
            'settings_file': os.path.join(BASE_DIR, 'drf_apis/drf_apis/settings.py')
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'drf_apis.urls'

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

WSGI_APPLICATION = 'drf_apis.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

from shutil import copyfile
src = os.path.join(BASE_DIR, 'db.sqlite3')
dst = "/tmp/db.sqlite3"
copyfile(src, dst)

DATABASES = {
    'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': dst
                }

#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'drf_baseball',
#        'USER': 'root',
#        'PASSWORD' : 'departed',
#        'HOST' : 'drfbaseball.cbi5ajkhmnug.us-east-2.rds.amazonaws.com',
##        'HOST': 'localhost',
#        'PORT' : '3306'
#    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
AWS_STORAGE_BUCKET_NAME = 'zappa-baseball-static'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3Boto3Storage'

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')


