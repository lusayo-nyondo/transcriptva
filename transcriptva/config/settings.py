import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-f4_pxd#$xbtg!$9^6d(0tnlz!ke-uazdeq89^c*3u^qrlbm$w2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'transcriptva.com',
    'cassacassa.pythonanywhere.com'
]

SITE_URL = 'http://localhost:8000'

# Application definition

# BLOG APP REMOVED BECAUSE THE BLOG APP WILL BE DEVELOPED IN WORDPRESS
INSTALLED_APPS = [
    'transcriptva_clientsite', # The main business website.
    'transcriptva_clienthub', # The client webapp for the platform.
    'transcriptva_clientsupport',
    'transcriptva_clientaccount',

    'transcriptva_admin', # Imports models from all dependent apps so include it last.

    ### DJANGO CMS STUFF FOR THE SUPPORT AND BLOG PARTS OF THE APP
    'sekizai',

    'cms',
    'menus',
    'treebeard',

    # 'djangocms_admin_style', # USELESS BECAUSE IT JUST MAKES THE SITE ADMIN UGLY
    
    # Plugins to make the administration interface look better
    # 'grappelli',

    'admin_interface',
    'colorfield',

    # CONTENT HANDLING STUFF FOR DJANGO CMS
    'easy_thumbnails',
    'mptt',
    'filer',

    'djangocms_text_ckeditor',
    'djangocms_link',
    'djangocms_file',
    'djangocms_picture',
    'djangocms_video',
    'djangocms_googlemap',
    'djangocms_snippet',
    'djangocms_style',

    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.humanize',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # MORE DJANGO CMS JUNK
    'django.middleware.locale.LocaleMiddleware',

    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'transcriptva/transcriptva_blog/templates',
            'transcriptva/transcriptva_clienthub/templates',
            'transcriptva/transcriptva_clientsite/templates',
            'transcriptva/transcriptva_clientsupport/templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # DJANGO CMS JUNK
                'django.template.context_processors.i18n',

                'cms.context_processors.cms_settings',
                'sekizai.context_processors.sekizai'
            ],
        },
    },
]

CMS_TEMPLATES = [
    ('transcriptva_clientsupport/index.dtl.html', 'Client Support Docs - CMS')
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', 'English')
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'public_static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'transcriptva_clientaccount.User'

MEDIA_URL = '/client_media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'client_media')

# DJANGO CMS JUNK AGAIN
SITE_ID = 1 #someone suggested django-cms-multisite as an alternative to this
X_FRAME_OPTIONS = 'SAMEORIGIN'

# MORE CONTENT STUFF FOR DJANGO CMS
THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

SILENCED_SYSTEM_CHECKS = ['security.W019']

# GRAPPELLI ADMINISTRATION SETTINGS

# GRAPPELLI_ADMIN_TITLE = 'Transcript VA'