
from pathlib import Path
import os




BASE_DIR = Path(__file__).resolve().parent.parent.parent
DEBUG = True
#DEBUG_PROPAGATE_EXCEPTIONS = True

#from .base_db import *


#--------------------------------------------------------------------------
# AWS S3
#--------------------------------------------------------------------------



# active is error -> why?  permission error?
#STATICFILES_STORAGE = 'config.settings.asset_storage.StaticRootS3Boto3Storage' # static

IS_MEDIA_PATH_3S = True




if DEBUG == False:
    AWS_ACCESS_KEY_ID = 'AKIAVTBEBJ5HEUGSVJXA'
    AWS_SECRET_ACCESS_KEY = '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'
    AWS_REGION = 'ap-northeast-2'
    AWS_STORAGE_BUCKET_NAME = 'amosioo-devjp'

    _AWS_EXPIRY = 60 * 60 * 24 * 7
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': f'max-age={_AWS_EXPIRY}, s-maxage={_AWS_EXPIRY}, must-revalidate',
    }

    DEFAULT_FILE_STORAGE = 'core.settings.aws_s3.MediaRootS3Boto3Storage' # media
    MEDIA_URL   = f'https://amosioo-devjp.s3.ap-northeast-2.amazonaws.com/media/'

    AWS_DEFAULT_ACL = None

    #STATICFILES_DIRS = [ str(os.path.join(BASE_DIR, 'data/static') )  , ]

    #STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    #STATIC_ROOT = str(os.path.join(BASE_DIR, 'data/staticfiles'))  # collectstatic path

    STATICFILES_DIRS = [str(os.path.join(BASE_DIR, 'data/static')), ] # ignore => no copy data/static : no serarch static
    STATICFILES_STORAGE = 'core.settings.aws_s3.StaticRootS3Boto3Storage' # static
    STATIC_URL   = 'https://amosioo-devjp.s3.ap-northeast-2.amazonaws.com/static/'
    #STATIC_ROOT =  'https://naver.com/static/'
    #STATIC_ROOT = str(os.path.join(BASE_DIR, 'data/staticfiles'))  # collectstatic path

else:
# ------------------------------------------------------------------------------

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.1/howto/static-files/

    MEDIA_ROOT = os.path.join(BASE_DIR, 'data/media/')
    MEDIA_URL = '/media/'


    STATIC_ROOT = str(os.path.join(BASE_DIR, 'data/staticfiles'))  # collectstatic path
    STATICFILES_DIRS = [ str(os.path.join(BASE_DIR, 'data/static') )  , ]
    STATIC_URL = '/static/'





ARBRE_URL = '/arbre/'

#--------------------------------------------------------------------------


BASE_DB_NAME = 'SQLITE'     # MYSQL SQLITE

if(BASE_DB_NAME == "MYSQL"):
    import pymysql

    pymysql.version_info = (1, 4, 13, "final", 0)  # must add
    pymysql.install_as_MySQLdb()

    DATABASES = {

        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'APPWEB2',
            'USER': 'admin',
            'PASSWORD': 'Leekyou7811#',
            'HOST': 'amoisoo-devjp.ceq425iwosr1.ap-northeast-2.rds.amazonaws.com',
            'PORT': '3306',
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            }
        }
    }
elif( BASE_DB_NAME == "SQLITE" ):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            # 'NAME': os.path.join(BASE_DIR, 'data/db5.sqlite3'),
            'NAME': os.path.join(BASE_DIR, 'jinyoung.sqlite3'), # base - db5.sqlite3 # usermodel_11
        }
    }



ALLOWED_HOSTS = ["*"]

WSGI_APPLICATION = 'core.wsgi.application'
ROOT_URLCONF = 'applications.main.urls'





#LOGIN_URL = 'accounts:login'
LOGIN_URL = '/accounts/login'
LOGOUT_URL = 'accounts:logout'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


AUTH_USER_MODEL = 'users.User'

THIRD_APPS = [

    'django_hosts', # sub domain
    'storages', # aws s3
]




LOCAL_APPS = [
    #'accounts.users.apps.UsersConfig',  # Error


    #'accounts.accounts.apps.AccountsConfig',

    'users.apps.UsersConfig',

    'applications.blog.apps.BlogConfig',
    'applications.support.apps.SupportConfig',
    'applications.sample.apps.SampleConfig',
    'applications.forum.apps.ForumConfig',
    'applications.book.apps.BookConfig',
    'applications.shelf.apps.ShelfConfig',
]








# Sub Doamin
ROOT_HOSTCONF = 'core.subdomain'
DEFAULT_HOST = 'www'
PARENT_HOST = 'amosoo.com'



