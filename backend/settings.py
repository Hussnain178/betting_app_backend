# """
# Django settings for your_project_name project.
# """
#
# from pathlib import Path
#
# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
#
# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
#
# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'your-secret-key-here'
#
# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
#
# ALLOWED_HOSTS = []
#
# # Application definition
#
# INSTALLED_APPS = [
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'rest_framework',            # Django REST Framework
#     'django_mongoengine',        # MongoDB integration
#     'users',             # Replace with your app name
# ]
#
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]
#
# ROOT_URLCONF = 'backend.urls'
#
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
#
# WSGI_APPLICATION = 'backend.wsgi.application'
#
# # Database
# # https://docs.djangoproject.com/en/4.2/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.dummy',  # Disables Django ORM
#     }
# }
#
# # MongoDB Configuration via django-mongoengine
# MONGODB_DATABASES = {
#     "default": {
#         "name": "betting",  # Replace with your MongoDB DB name
#         "host": "localhost",           # MongoDB server host
#         "port": 27017,                 # MongoDB server port
#         # Optional (if using authentication)
#         # "username": "your_user",
#         # "password": "your_password",
#         # "authentication_source": "admin",
#     }
# }
#
# # Password validation
# #  https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
#
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]
#
# # Internationalization
# #  https://docs.djangoproject.com/en/4.2/topics/i18n/
#
# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'UTC'
#
# USE_I18N = True
#
# USE_TZ = True
#
# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/4.2/howto/static-files/
#
# STATIC_URL = 'static/'
#
# # Default primary key field type
# # https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
#
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# settings.py

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", "fallback_secret_key")
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_mongoengine',          # MongoDB ORM
    'django_mongoengine.mongo_auth',  # Mongo-based auth
    'users',
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

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'

# Disable Django ORM
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy',
    }
}

# MongoDB Configuration
MONGODB_DATABASES = {
    "default": {
        "name": "betting",
        "host": "localhost",
        "port": 27017,
    }
}

AUTH_USER_MODEL = 'mongo_auth.MongoUser'
AUTHENTICATION_BACKENDS = [
    'django_mongoengine.mongo_auth.backends.MongoAuthBackend',
]
MONGOENGINE_USER_DOCUMENT = 'users.models.User'

# Session Fix: Use cookie-based sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'