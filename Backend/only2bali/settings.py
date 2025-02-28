"""
Django settings for only2bali project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-#%+v7yrj)fqc9@w8=tf^1blsr@x#p!3b+0=@%3%m3tqi)a9xr0"
# AVIATIONSTACK_API_KEY = '77a30f0f78f6d8f3e75b6089a9427308'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# Email configuration (adjust for your email service provider)
# #EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Use SMTP for real emails
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'  # Change to your email service provider
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'samplebali121@gmail.com'  # Use your email here
# EMAIL_HOST_PASSWORD = 'pado vlom rabv kddy'  # Use your email password
# # DEFAULT_FROM_EMAIL = 'your-email@gmail.com'  # Default sender email


# Email configuration (adjust for your email service provider)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Use SMTP for real emails
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.zoho.com'  # Change to your email service provider
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'admin@only2bali.com'  # Use your email here
EMAIL_HOST_PASSWORD = 'S3cur3@Bali'  # Use your email password
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # Default sender email


FRONTEND_URL = 'http://localhost:3000'  # Frontend URL for the reset page



TWILIO_PHONE_NUMBER='+1 915 277 6125'

ALLOWED_HOSTS = [ 'localhost', '127.0.0.1' , 'https://happy-dune-02aab6b00.6.azurestaticapps.net']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    'django.contrib.sites',
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'users',
    'journeys',
    'django_extensions',
    'corsheaders',#for react 
]
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),  # Set access token expiry time to 60 minutes
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),     # Set refresh token expiry time to 1 day
    'ROTATE_REFRESH_TOKENS': False,                   # Optional: Rotate refresh tokens on refresh
    'BLACKLIST_AFTER_ROTATION': True,                 # Optional: Blacklist old refresh tokens
}
SITE_ID = 1
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
# CORS_ORIGIN_WHITELIST = [
#     'http://localhost:3000',
# ]

CORS_ALLOWED_ORIGINS = [
    # "http://192.168.1.7:3000",
    # "http://103.197.112.7:8000" ,
    # "http://192.168.1.14:8000",
      "http://127.0.0.1:8000", # React app running on another laptop
      "http://localhost:3000",
      "https://happy-dune-02aab6b00.6.azurestaticapps.net"
    #   "http://192.168.1.14:3000",
]
CORS_ALLOW_HEADERS = [
    'content-type',
    'Authorization',
    'x-csrftoken',
    # Add other headers you need to allow
]
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',  # Ensure OPTIONS is allowed
]

ROOT_URLCONF = "only2bali.urls"
AUTH_USER_MODEL = 'users.CustomUser'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'static')],
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

WSGI_APPLICATION = "only2bali.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ONLY2BALI',  # Replace with your database name
        'USER': 'BALI',  # Replace with your database user
        'PASSWORD': 'only2bali@1234',  # Replace with your password
        'HOST': 'localhost',  # Use the database server's address (default is localhost)
        'PORT': '5432',  # Default PostgreSQL port
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
# settings.py


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',  # In-memory cache for testing
      #  'TIMEOUT': 300,  # 5 minutes timeout for OTP
    }
}


