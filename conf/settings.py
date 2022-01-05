from pathlib import Path
import os
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!&9y0b^^=&8-g+qh(0xugg8r%245aq+-w12@qkt+k@%2+x&d1r'

ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS=True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = [
    "http://127.0.0.1",
    "http://127.0.0.1:3000",
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    
    'nezbank',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'drf_yasg',
    'django_extensions',
    'django.contrib.admin',  
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
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

WSGI_APPLICATION = 'conf.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
    }
}
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
    { 'NAME': 'nezbank.authutils.PasswordCharsValidator', },
]


TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru-ru'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEBUG = True

SWAGGER_SETTINGS = {
   'USE_SESSION_AUTH': False
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    )
}

AUTH_USER_MODEL = 'nezbank.User'
REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'nezbank.serializers.LoginSerializer'
    }

REST_USE_JWT = True
JWT_AUTH_COOKIE = 'Bearer'
SIMPLE_JWT = {
    'BLACKLIST_AFTER_ROTATION': False,
    'ACCESS_TOKEN_LIFETIME': timedelta(days=365),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=365),
    }
JWT_AUTH_SAMESITE = None

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_VERIFICATION_URL = "http://localhost:8000/email-verification/"
EMAIL_FROM = 'no-reply@testbank.ru'

# SENTRY_DSN = os.environ.get('SENTRY_DSN', None)
# if SENTRY_DSN:
#     import sentry_sdk
#     from sentry_sdk.integrations.django import DjangoIntegration

#     sentry_sdk.init(
#         dsn=SENTRY_DSN,
#         integrations=[DjangoIntegration()],

#         # Set traces_sample_rate to 1.0 to capture 100%
#         # of transactions for performance monitoring.
#         # We recommend adjusting this value in production,
#         traces_sample_rate=1.0,

#         # If you wish to associate users to errors (assuming you are using
#         # django.contrib.auth) you may enable sending PII data.
#         send_default_pii=True,
#     )
