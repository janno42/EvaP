# -*- coding: utf-8 -*-
"""
Django settings for EvaP project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
import sys
from django.contrib.messages import constants as messages

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


### Debugging

DEBUG = True

TEMPLATE_DEBUG = DEBUG

# Very helpful but eats a lot of performance on sql-heavy pages.
# Works only with DEBUG = True.
ENABLE_DEBUG_TOOLBAR = False


### EvaP logic

# key authentication settings
LOGIN_KEY_VALIDITY = 210 # days, so roughly 7 months

# minimum answers needed for publishing
MIN_ANSWER_COUNT = 2
MIN_ANSWER_PERCENTAGE = 0.2

# a warning is shown next to results where less than this percentage of the median number of answers (for this question in this course) were given
RESULTS_WARNING_PERCENTAGE = 0.5

# the final total grade will be calculated by the following formula (GP = GRADE_PERCENTAGE, CP = CONTRIBUTION_PERCENTAGE):
# final_likert = CP * likert_answers_about_persons + (1-CP) * likert_answers_about_courses
# final_grade = CP * grade_answers_about_persons + (1-CP) * grade_answers_about_courses
# final = GP * final_grade + (1-GP) * final_likert
GRADE_PERCENTAGE = 0.8
CONTRIBUTION_PERCENTAGE = 0.5

# number of reward points to be given to a student once all courses of a semester have been voted for
REWARD_POINTS_PER_SEMESTER = 3

# days before end date to send reminder
REMIND_X_DAYS_AHEAD_OF_END_DATE = [2, 0]

# email domains for the internal users of the hosting institution used to
# figure out who can login with username and password and who needs a login key
INSTITUTION_EMAIL_DOMAINS = ["hpi.uni-potsdam.de", "student.hpi.uni-potsdam.de", "hpi.de", "student.hpi.de"]

# maximum length of usernames of internal users
INTERNAL_USERNAMES_MAX_LENGTH = 20

# the importer accepts only these two strings in the 'graded' column
IMPORTER_GRADED_YES = "yes"
IMPORTER_GRADED_NO = "no"


### Installation specific settings

# People who get emails on errors.
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

ALLOWED_HOSTS = []

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'k9-)vh3c_dtm6bpi7j(!*s_^91v0!ekjt_#o&0i$e22tnn^-vb'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(BASE_DIR, 'database.sqlite3'), # Or path to database file if using sqlite3.
        'USER': '',                             # Not used with sqlite3.
        'PASSWORD': '',                         # Not used with sqlite3.
        'HOST': '',                             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                             # Set to empty string for default. Not used with sqlite3.
    }
}

# Config for feedback links
FEEDBACK_EMAIL = "webmaster@localhost"
TRACKER_URL = "https://github.com/fsr-itse/EvaP"

# Config for mail system
DEFAULT_FROM_EMAIL = "webmaster@localhost"
REPLY_TO_EMAIL = DEFAULT_FROM_EMAIL
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Kerberos realm and service
ENABLE_KERBEROS = False
if (ENABLE_KERBEROS):
    KRB5_REALM = 'EXAMPLE.COM'
    KRB5_SERVICE = 'krbtgt@AS.EXAMPLE.COM'
    INSTALLED_APPS += ('django_auth_kerberos',)
    MIDDLEWARE_CLASSES += ('django_auth_kerberos.backends.KrbBackend',)


### Application definition

AUTH_USER_MODEL = 'evaluation.UserProfile'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', # unused. left here to not break the test data.
    'widget_tweaks',
    'evap.evaluation',
    'evap.staff',
    'evap.results',
    'evap.student',
    'evap.contributor',
    'evap.rewards',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'evap.evaluation.auth.RequestAuthMiddleware',
    'evap.evaluation.403.Django403Middleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
)

AUTHENTICATION_BACKENDS = (
    'evap.evaluation.auth.RequestAuthUserBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Additional locations of templates
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)

ROOT_URLCONF = 'evap.urls'

WSGI_APPLICATION = 'evap.wsgi.application'

# Redirect url after login
LOGIN_REDIRECT_URL = '/'

LOGIN_URL = "/"


### Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = False

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"),
)

LANGUAGES = (
    ('en', "English"),
    ('de', "Deutsch"),
)

USERNAME_REPLACEMENTS = [
    (' ', ''),
    (u'ä', 'ae'),
    (u'ö', 'oe'),
    (u'ü', 'ue'),
    (u'ß', 'ss'),
]


### Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# Absolute path to the directory static files should be collected to.
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


### User-uploaded files

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = os.path.join(BASE_DIR, "upload")

# URL that handles the media served from MEDIA_ROOT.
MEDIA_URL = '/media/'


### Other

# Apply the correct bootstrap css class to django's error messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

# Django debug toolbar settings
TESTING = 'test' in sys.argv
if DEBUG and not TESTING and ENABLE_DEBUG_TOOLBAR:
    DEBUG_TOOLBAR_PATCH_SETTINGS = False
    INSTALLED_APPS += ('debug_toolbar',)
    MIDDLEWARE_CLASSES = ('debug_toolbar.middleware.DebugToolbarMiddleware',) + MIDDLEWARE_CLASSES
    def show_toolbar(request):
        return True
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': 'evap.settings.show_toolbar',
    }


# Create a localsettings.py if you want to locally override settings
# and don't want the changes to appear in 'git status'.
_LOCAL_SETTINGS_FILENAME = os.path.join(BASE_DIR, "localsettings.py")
if os.path.exists(_LOCAL_SETTINGS_FILENAME):
    exec(compile(open(_LOCAL_SETTINGS_FILENAME).read(), _LOCAL_SETTINGS_FILENAME, 'exec'))
del _LOCAL_SETTINGS_FILENAME
