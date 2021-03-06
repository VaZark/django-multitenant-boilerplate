"""
Django settings for multitenant project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-&kjvvyl+ozf7$y9%o-6&3(y5*4=a7m^b)96lxgo6xyiyyfe+7s"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


HAS_MULTI_TYPE_TENANTS = True
MULTI_TYPE_DATABASE_FIELD = "tenant_type"

# Application definition
TENANT_TYPES = {
    "public": {  # this is the name of the public schema from get_public_schema_name
        "APPS": [
            "django_tenants",
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "django.contrib.staticfiles",
            # shared apps here
            "users",
            "owner",
        ],
        "URLCONF": "owner.urls",  # url for the public type here
    },
    "crm": {
        "APPS": [
            "django.contrib.contenttypes",
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.sessions",
            "django.contrib.messages",
            # crm apps here
            "users",
            "tenant",
        ],
        "URLCONF": "tenant.urls",
    },
}

TENANT_MODEL = "owner.Tenant"
TENANT_DOMAIN_MODEL = "owner.Domain" 
TENANT_COLOR_ADMIN_APPS = False

INSTALLED_APPS = []
for schema in TENANT_TYPES:
    INSTALLED_APPS += [app for app in TENANT_TYPES[schema]["APPS"] if app not in INSTALLED_APPS]

if DEBUG:
    INSTALLED_APPS += ["django_extensions"]

DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}

MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "multitenant.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "multitenant.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE" : "django_tenants.postgresql_backend",
        # "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "testdb",
        "USER": "postgres",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "5432",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


STATIC_URL = "static/"
STATIC_ROOT = "static"
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "users.CustomUser"