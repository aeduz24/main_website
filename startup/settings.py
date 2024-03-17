"""
Django settings for startup project.

Generated by 'django-admin startproject' using Django 4.2.10.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-n^x!sf$&m*___8yl0)yse#xo-r6628#zxq@=sasy@3%417(v@c"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS =  ['www.aeduz.com','aeduz.com','13.126.66.72','localhost','127.0.0.1']



# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "insti_app",
    "book",
    "allauth",   
    "allauth.account",  
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google", 
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

AUTHENTICATION_BACKENDS = ( 'django.contrib.auth.backends.ModelBackend', 'allauth.account.auth_backends.AuthenticationBackend', )
SITE_ID = 2
LOGIN_REDIRECT_URL = '/dashboard'


SOCIALACCOUNT_PROVIDERS = { 'google': { 'SCOPE': [ 'profile', 'email', ], 'AUTH_PARAMS': { 'access_type': 'online', } } }

ROOT_URLCONF = "startup.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ['templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "startup.wsgi.application"
import os 
STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# STATICFILES_DIRS = [
#     os.path.join('var/www/aakar/static', 'static'),
#    os.path.join(BASE_DIR,'static')
    
# ]
# Database https://docs.djangoproject.com/en/4.2/ref/settings/#databases
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'static'),

]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

#STATIC_URL = "static/"
#STATIC_R
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

from django.contrib.messages import constants as c 
MESSAGE_TAGS={
    c.ERROR:'danger'
}
