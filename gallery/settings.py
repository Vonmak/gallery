"""
Django settings for gallery project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import django_heroku
import dj_database_url
from decouple import config,Csv

import cloudinary
import cloudinary.uploader
import cloudinary.api

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/


MODE=config("MODE", default="dev")
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '310aa7621f7c8b6217e2c7574b9bd2c021a2452508012d02710df8a4328bc07b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False
# ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
ALLOWED_HOSTS=['*']


# Application definition

INSTALLED_APPS = [
    
    'colBox',
    "bootstrap5",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'gallery.urls'

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
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'gallery.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# development
# if config('MODE')=="dev":
DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'railway',
           'USER': 'postgres',
           'PASSWORD': 'nEIV4CIZ8XAsYzxkbAEH',
           'HOST': 'containers-us-west-161.railway.app',
           'PORT': '7018',
       }
       
   }
# production
# else:
#    DATABASES = {
#        'default': dj_database_url.config(
#            default=config('DATABASE_URL')
#        )
#    }

# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/


# STATIC_URL = 'static/'

# Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
# STATIC_ROOT=os.path.join(BASE_DIR,"/static/") 

# STATIC_ROOT = '/Users/vic/Documents/django/theGallery/static',


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = 'static/'
STATIC_FILES_DIRS = [os.path.join(BASE_DIR, 'static')],
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')




# Whitenoise Settings
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATICFILES_STORAGE =  'django.contrib.staticfiles.storage.StaticFilesStorage'


# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Configure Django App for Heroku.
# django_heroku.settings(locals())

# adding config
cloudinary.config( 
  cloud_name = "ddtmsdlip", 
  api_key = "356757256393764", 
  api_secret = "V-68rzwrl7fFATIiLhanN9z8zts" 
)
