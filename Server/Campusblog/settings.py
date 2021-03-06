"""
Django settings for Campusblog project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from typing import OrderedDict
from os import path

# from constance import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

AUTH_USER_MODEL = "Campusauth.User"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "rft@o#j5wcwm-6&gh658(s(w6(z^)e)l8r8y2cjli3=234s&=9"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "corsheaders",
    "import_export",
    "simpleui",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "djoser",
    "Campusblog",
    "Campusauth",
    "Campusblogs",
    "rest_framework",
    "rest_framework.authtoken",
    "martor",
    "constance",
    "constance.backends.database",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "Campusblog.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [path.join(BASE_DIR, "templates")],
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

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
        "rest_framework_rapidjson.renderers.RapidJSONRenderer",
        "rest_framework_msgpack.renderers.MessagePackRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.MultiPartParser",
        "rest_framework_rapidjson.parsers.RapidJSONParser",
        "rest_framework_msgpack.parsers.MessagePackParser",
    ],
}

WSGI_APPLICATION = "Campusblog.wsgi.application"

########################################################################
# 数据库
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
########################################################################
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'django',
#         'USER': 'django',
#         "PASSWORD": 'django',
#         'HOST': "127.0.0.1"
#     }
# }

########################################################################
# 缓存
########################################################################
CACHES = {"default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"}}
# CONSTANCE_DATABASE_CACHE_BACKEND = 'default'
########################################################################
#
# 验证方案
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
#
########################################################################

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

########################################################################
# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/
########################################################################

LANGUAGE_CODE = "zh-Hans"

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_L10N = True

USE_TZ = True

########################################################################
# 静态文件
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
########################################################################

STATIC_URL = "/static/"
STATIC_ROOT = "static/collectstatic"
STATICFILES_DIRS = [BASE_DIR / "static"]

########################################################################
#
# CORS设置
#
########################################################################

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_ALL_ORIGINS = True
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
    "WWW-Authenticate",
]


#####################################################################################
#
#   网站设置
#
#####################################################################################
CONSTANCE_BACKEND = "constance.backends.database.DatabaseBackend"
CONSTANCE_IGNORE_ADMIN_VERSION_CHECK = True

CONSTANCE_CONFIG = {
    "site_name": ("校园博客", "网站标题"),
    "site_description": ("校园博客", "站点描述"),
    "sensitive_words": ("", "敏感词"),
}

CONSTANCE_CONFIG_FIELDSETS = OrderedDict(
    [("站点设置", ("site_name", "site_description")), ("敏感词设置", ("sensitive_words",))]
)

#####################################################################################
#
#   后台设置
#
#####################################################################################

# SIMPLEUI_HOME_PAGE = getattr(config,'site_name')

SIMPLEUI_DEFAULT_ICON = False
SIMPLEUI_STATIC_OFFLINE = True
SIMPLEUI_HOME_INFO = False

SIMPLEUI_CONFIG = {
    "dynamic": False,
    "system_keep": False,
    "menus": [
        {
            "name": "会员管理",
            "icon": "fab fa-microsoft",
            "models": [
                {
                    "name": "用户管理",
                    "app": "Campusauth",
                    "icon": "far fa-user",
                    "url": "/admin/Campusauth/user/",
                },
                {
                    "name": "用户组管理",
                    "app": "auth",
                    "icon": "fas fa-users-cog",
                    "url": "/admin/auth/group/",
                },
            ],
        },
        {
            "name": "内容管理",
            "icon": "fas fa-globe-americas",
            "models": [
                {
                    'name': '分类管理',
                    "app": "Campusblogs",
                    "url": "/admin/Campusblogs/classify",
                },
                {
                    "name": "文章管理",
                    "app": "Campusblogs",
                    "url": "/admin/Campusblogs/blogs",
                },
                {
                    "name": "举报管理",
                    "app": "Campusblogs",
                    "url": "/admin/Campusblogs/reports"
                },
                {
                    "name": "回复管理",
                    "app": "Campusblogs",
                    "url": "/admin/Campusblogs/posts",
                },
            ],
        },
        {
            "name": "系统设置",
            "models": [
                {
                    "name": "网站设置",
                    "url": "/admin/constance/config/"
                },
                {
                    "name": "公告管理",
                    "url": "/admin/Campusblogs/notices",
                }
            ]
        }
    ],
}

IMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer", "JWT"),
}

#####################################################################################
#
#   DJOSER 设置
#
#####################################################################################

DJOSER = {
    "SERIALIZERS": {"current_user": "Campusauth.serializers.UserSerializer"},
    # 'LOGIN_FIELD': 'avatar'
}
#####################################################################################