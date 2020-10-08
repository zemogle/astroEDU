"""
Django settings for astroedu project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
from django_storage_url import dsn_configured_storage_class


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'z2=$*^40@k+--2u@z8j8&c5!^3_o1-lc06#ih5^uboqtn(*1n0')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG') == "True"

DIVIO_DOMAIN = os.environ.get('DOMAIN', '')

DIVIO_DOMAIN_ALIASES = [
    d.strip()
    for d in os.environ.get('DOMAIN_ALIASES', '').split(',')
    if d.strip()
]

ALLOWED_HOSTS = [DIVIO_DOMAIN] + DIVIO_DOMAIN_ALIASES


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'parler',
    'ckeditor',
    # 'sorl.thumbnail',
    'easy_thumbnails',

    'django_mistune',

    'django_ext',
    'smartpages',
    'institutions',
    'activities',
    'filemanager',
    'astroedu',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
   'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'astroedu.urls'

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

WSGI_APPLICATION = 'astroedu.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DEFAULT_DATABASE_DSN = os.environ.get('DEFAULT_DATABASE_DSN', 'sqlite://:memory:')
DATABASES = {'default': dj_database_url.parse(DEFAULT_DATABASE_DSN)}

CKEDITOR_UPLOAD_PATH = 'upload/'
CKEDITOR_CONFIGS = {
    ## see http://docs.cksource.com/CKEditor_3.x/Developers_Guide/Toolbar
    'smartpages': {
        'fillEmptyBlocks': False,
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Source', ],
            ['Format', ],
            ['Bold', 'Italic', '-', 'Underline', 'Subscript', 'Superscript', '-', 'Undo', 'Redo', 'RemoveFormat', ],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', ],
            ['Link', 'Unlink', ],
            ['Image', 'Table', 'SpecialChar', ],
            ['Maximize', 'ShowBlocks', ],
            ['BidiLtr', 'BidiRtl', ],
        ],
        'width': 845,
    },
    'small': {
        'fillEmptyBlocks': False,
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Source', ],
            ['Bold', 'Italic', '-', 'Subscript', 'Superscript', '-', 'Undo', 'Redo', 'RemoveFormat', ],
            ['Link', 'Unlink', ],
            # ['Image', ],
            ['BidiLtr', 'BidiRtl', ],
        ],
        'height': 100,
    },

}
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = (
    # ('cs', 'Czech'),
    # ('nl', 'Dutch'),
    ('en', 'English'),
    # ('fr', 'French'),
    # ('de', 'German'),
    # ('el', 'Greek'),
    ('it', 'Italian'),
    ('kr', 'Korean'),
)
# LANGUAGES = sorted(LANGUAGES, key=operator.itemgetter(0))

PARLER_LANGUAGES = {
    1: (
        {'code': 'en'},
        {'code': 'it'},
        {'code': 'kr'},
    ),
    'default': {
        'fallbacks': ['en'],
        'hide_untranslated': True,   # False is the default; let .active_translations() return fallbacks too.
    }
}

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# read the setting value from the environment variable
DEFAULT_STORAGE_DSN = os.environ.get('DEFAULT_STORAGE_DSN')

# dsn_configured_storage_class() requires the name of the setting
DefaultStorageClass = dsn_configured_storage_class('DEFAULT_STORAGE_DSN')

# Django's DEFAULT_FILE_STORAGE requires the class name
DEFAULT_FILE_STORAGE = 'astroedu.settings.DefaultStorageClass'

THUMBNAIL_DEFAULT_STORAGE  = DEFAULT_FILE_STORAGE

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join('/data/media/')

THUMBNAIL_ALIASES = {
    '': {
        'thumb': {'size': (334, 180), 'crop': True},
        'thumb2': {'size': (500, 269), 'crop': True},
        'epubcover': {'size': (800,1066), 'crop': True},
        'logo': {'size': (180, 180), 'crop': 'scale'},
        },
}
