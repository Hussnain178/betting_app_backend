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

# import os
# from pathlib import Path
# from dotenv import load_dotenv
#
# load_dotenv()
#
# BASE_DIR = Path(__file__).resolve().parent.parent
#
# SECRET_KEY = os.getenv("SECRET_KEY", "fallback_secret_key")
# DEBUG = True
# ALLOWED_HOSTS = ['*']
# # ALLOWED_HOSTS = []
#
# INSTALLED_APPS = [
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'rest_framework',
#     'django_mongoengine',          # MongoDB ORM
#     'django_mongoengine.mongo_auth',  # Mongo-based auth
#     'users',
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
# # Disable Django ORM
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.dummy',
#     }
# }
#
# # MongoDB Configuration
# MONGODB_DATABASES = {
#     "default": {
#         "name": "betting",
#         "host": "localhost",
#         "port": 27017,
#     }
# }
#
# AUTH_USER_MODEL = 'mongo_auth.MongoUser'
# AUTHENTICATION_BACKENDS = [
#     'django_mongoengine.mongo_auth.backends.MongoAuthBackend',
# ]
# MONGOENGINE_USER_DOCUMENT = 'users.models.User'
#
# # Session Fix: Use cookie-based sessions
# SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
#
# # Password validation
# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
# ]
#
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True
#
# STATIC_URL = 'static/'
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#

# # running one
# import os
# from pathlib import Path
# from dotenv import load_dotenv
#
# load_dotenv()
#
# BASE_DIR = Path(__file__).resolve().parent.parent
#
# # Security Settings
# SECRET_KEY = os.getenv("SECRET_KEY", "fallback_secret_key")
# DEBUG = True
# ALLOWED_HOSTS = ["*"]  # For development only
#
# # CORS Configuration (Allow all origins for development)
# CORS_ALLOW_ALL_ORIGINS = True  # ⚠️ Not safe for production!
# CORS_ALLOWED_ORIGINS = []  # Ignored when CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOW_CREDENTIALS = True  # Allow cookies/auth headers
# CORS_ALLOW_METHODS = [
#     "GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"
# ]
# CORS_ALLOW_HEADERS = [
#     "accept", "accept-encoding", "authorization", "content-type",
#     "dnt", "origin", "user-agent", "x-csrftoken", "x-requested-with"
# ]
# CSRF_TRUSTED_ORIGINS = ["http://localhost:3000"]  # Match your frontend URL
#
# # Django Applications
# INSTALLED_APPS = [
#     'corsheaders',  # Must come first
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'rest_framework',
#     'django_mongoengine',
#     'django_mongoengine.mongo_auth',
#     'users',
#     'matches_data'
# ]
#
# # Middleware
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'corsheaders.middleware.CorsMiddleware',  # Must come early
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]
#
# # URLs and Templates
# ROOT_URLCONF = 'backend.urls'
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
# # Database (MongoDB via Django-MongoEngine)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.dummy',
#     }
# }
#
# MONGODB_DATABASES = {
#     "default": {
#         "name": "betting",
#         "host": "localhost",
#         "port": 27017,
#     }
# }
#
# # Authentication
# AUTH_USER_MODEL = 'mongo_auth.MongoUser'
# AUTHENTICATION_BACKENDS = [
#     'django_mongoengine.mongo_auth.backends.MongoAuthBackend',
# ]
# MONGOENGINE_USER_DOCUMENT = 'users.models.User'
#
# # Session Configuration
# SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
# SESSION_COOKIE_SAMESITE = 'None'  # Allow cross-origin cookies
# SESSION_COOKIE_SECURE = False  # Set to True if using HTTPS
#
# # Password Validation
# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
# ]
#
# # Internationalization
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True
#
# # Static Files
# STATIC_URL = 'static/'
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#
#
# settings.py - CORS Configuration Fix

# import os
# from pathlib import Path
# from dotenv import load_dotenv
#
# load_dotenv()
#
# BASE_DIR = Path(__file__).resolve().parent.parent
#
# # Security Settings
# SECRET_KEY = os.getenv("SECRET_KEY", "fallback_secret_key")
# DEBUG = True
# ALLOWED_HOSTS = ["*"]  # For development only
#
# # CORS Configuration - FIXED
# CORS_ALLOW_ALL_ORIGINS = False  # ❌ Change this to False
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",    # React default
#     "http://localhost:5173",    # Vite default
#     "http://127.0.0.1:3000",
#     "http://127.0.0.1:5173",
#     # Add your ngrok URL if needed for testing
#     # "https://your-ngrok-url.ngrok-free.app",
# ]
# CORS_ALLOW_CREDENTIALS = True  # Keep this True for auth
# CORS_ALLOW_METHODS = [
#     "GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"
# ]
# CORS_ALLOW_HEADERS = [
#     "accept", "accept-encoding", "authorization", "content-type",
#     "dnt", "origin", "user-agent", "x-csrftoken", "x-requested-with",
#     "cache-control"
# ]
#
# # CSRF Configuration
# CSRF_TRUSTED_ORIGINS = [
#     "http://localhost:3000",
#     "http://localhost:5173",
#     "http://127.0.0.1:3000",
#     "http://127.0.0.1:5173"
# ]
#
# # Django Applications
# INSTALLED_APPS = [
#     'corsheaders',  # Must come first
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'rest_framework',
#     'django_mongoengine',
#     'django_mongoengine.mongo_auth',
#     'users',
#     'matches_data'
# ]
#
# # Middleware
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'corsheaders.middleware.CorsMiddleware',  # Must come early
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]
#
# # URLs and Templates
# ROOT_URLCONF = 'backend.urls'
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
# # Database (MongoDB via Django-MongoEngine)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.dummy',
#     }
# }
#
# MONGODB_DATABASES = {
#     "default": {
#         "name": "betting",
#         "host": "localhost",
#         "port": 27017,
#     }
# }
#
# # Authentication
# AUTH_USER_MODEL = 'mongo_auth.MongoUser'
# AUTHENTICATION_BACKENDS = [
#     'django_mongoengine.mongo_auth.backends.MongoAuthBackend',
# ]
# MONGOENGINE_USER_DOCUMENT = 'users.models.User'
#
# # Session Configuration
# SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
# SESSION_COOKIE_SAMESITE = 'Lax'  # Changed from 'None' for better security
# SESSION_COOKIE_SECURE = False  # Set to True if using HTTPS
# SESSION_COOKIE_HTTPONLY = True
#
# # Password Validation
# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
# ]
#
# # Internationalization
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True
#
# # Static Files
# STATIC_URL = 'static/'
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# settings.py - Complete CORS Fix with Debugging

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# Security Settings
SECRET_KEY = os.getenv("SECRET_KEY", "fallback_secret_key")
DEBUG = True
ALLOWED_HOSTS = ['144.172.94.64', 'localhost', '127.0.0.1']

# CORS Configuration - Complete Fix
CORS_ALLOW_ALL_ORIGINS = False  # Must be False
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = [
    "GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"
]
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "cache-control",
    "x-forwarded-for",
    "x-forwarded-proto",
]

# Additional CORS settings for better compatibility
CORS_PREFLIGHT_MAX_AGE = 86400
CORS_EXPOSE_HEADERS = [
    "content-type",
    "x-csrftoken",
]

# CSRF Configuration
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
]

# Disable CSRF for API endpoints (alternative approach)
CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False
CSRF_USE_SESSIONS = False

# Django Applications
INSTALLED_APPS = [
    'corsheaders',  # MUST be first
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_mongoengine',
    'django_mongoengine.mongo_auth',
    'users',
    'matches_data'
]

# Middleware - Order is crucial
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # MUST be first
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# REST Framework Configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}

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

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy',
    }
}

MONGODB_DATABASES = {
    "default": {
        "name": "betting",
        "host": "localhost",
        "port": 27017,
    }
}

# Authentication
AUTH_USER_MODEL = 'mongo_auth.MongoUser'
AUTHENTICATION_BACKENDS = [
    'django_mongoengine.mongo_auth.backends.MongoAuthBackend',
]
MONGOENGINE_USER_DOCUMENT = 'users.models.User'

# Session Configuration
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
SESSION_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = True

# Logging for debugging CORS
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'corsheaders': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Password Validation
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

# import os
# from pathlib import Path
# from dotenv import load_dotenv
#
# load_dotenv()
#
# BASE_DIR = Path(__file__).resolve().parent.parent
#
# # Security Settings
# SECRET_KEY = os.getenv("SECRET_KEY", "fallback_secret_key")
# DEBUG = True
# ALLOWED_HOSTS = ["*"]  # Allow all hosts
#
# # CORS Configuration - Allow all origins and methods
# CORS_ALLOW_ALL_ORIGINS = True  # This allows any origin
# CORS_ALLOW_CREDENTIALS = True  # Allow cookies/auth headers
# CORS_ALLOW_METHODS = [
#     "DELETE",
#     "GET",
#     "OPTIONS",
#     "PATCH",
#     "POST",
#     "PUT",
# ]
# CORS_ALLOW_HEADERS = [
#     "accept",
#     "accept-encoding",
#     "authorization",
#     "content-type",
#     "dnt",
#     "origin",
#     "user-agent",
#     "x-csrftoken",
#     "x-requested-with",
#     "x-forwarded-for",
#     "x-forwarded-proto",
# ]
#
# # Additional CORS settings for maximum compatibility
# CORS_ALLOWED_ORIGIN_REGEXES = [
#     r"^https?://.*$",  # Allow any HTTP/HTTPS origin
# ]
#
# # CSRF Settings - More permissive for development
# CSRF_TRUSTED_ORIGINS = [
#     "http://localhost:3000",
#     "https://localhost:3000",
#     "http://127.0.0.1:3000",
#     "https://127.0.0.1:3000",
# ]
# CSRF_COOKIE_SAMESITE = 'None'
# CSRF_COOKIE_SECURE = False  # Set to True in production with HTTPS
# CSRF_COOKIE_HTTPONLY = False
#
# # Django Applications
# INSTALLED_APPS = [
#     'corsheaders',  # Must come first
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'rest_framework',
#     'django_mongoengine',
#     'django_mongoengine.mongo_auth',
#     'users',
#     'matches_data'
# ]
#
# # Middleware - Order is important
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'corsheaders.middleware.CorsMiddleware',  # Must be at the top
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'backend.middleware.CSRFExemptMiddleware',
# ]
#
# # URLs and Templates
# ROOT_URLCONF = 'backend.urls'
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
# # Database (MongoDB via Django-MongoEngine)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.dummy',
#     }
# }
#
# MONGODB_DATABASES = {
#     "default": {
#         "name": "betting",
#         "host": "localhost",
#         "port": 27017,
#     }
# }
#
# # Authentication
# AUTH_USER_MODEL = 'mongo_auth.MongoUser'
# AUTHENTICATION_BACKENDS = [
#     'django_mongoengine.mongo_auth.backends.MongoAuthBackend',
# ]
# MONGOENGINE_USER_DOCUMENT = 'users.models.User'
#
# # Session Configuration - More permissive
# SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
# SESSION_COOKIE_SAMESITE = 'None'  # Allow cross-origin cookies
# SESSION_COOKIE_SECURE = False  # Set to True if using HTTPS
# SESSION_COOKIE_HTTPONLY = False  # Allow JavaScript access if needed
# SESSION_SAVE_EVERY_REQUEST = True
#
# # Security Settings - Relaxed for development
# SECURE_CROSS_ORIGIN_OPENER_POLICY = None
# X_FRAME_OPTIONS = 'SAMEORIGIN'  # or 'DENY' for more security
#
# # Password Validation
# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
# ]
#
# # Internationalization
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True
#
# # Static Files
# STATIC_URL = 'static/'
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#
# # Django REST Framework settings (if you're using DRF)
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.SessionAuthentication',
#         'rest_framework.authentication.BasicAuthentication',
#     ],
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.AllowAny',  # Very permissive - adjust as needed
#     ],
# }
