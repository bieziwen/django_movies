
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
"""
第一步

在实战开发中,经常讲app规整到一个文件夹下
第一步 在根目录创建apps目录
第二歩 创建的app移动到apps中
第三步  将apps文件设置 source root
第四步 在settings 中加入  sys.path.insert(0,os.path.join(BASE_DIR,'apps'))
注意事项
注册app的时候一定要加上apps目录

第二歩
二级路由配置

第三歩  其他配置
 静态文件的配置
 修改数据配置
 修改语言
 修改时区
"""


SECRET_KEY = '*re-o4cl_)&(%43(vfd!*&8hh91+%m^!6exl_3cv)2ax%56xm('

DEBUG = True

ALLOWED_HOSTS = []

sys.path.insert(0,os.path.join(BASE_DIR,'apps'))

SYS_APPS=[
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
MY_APPS=[
    'apps.home',
    'apps.account',
]
EXP_APPS=[]

INSTALLED_APPS =SYS_APPS+MY_APPS+EXP_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_movies.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # '......day07.account.context_processors.uname',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_movies.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
"""
sqi_mode有三种选项

ANSI 宽松模式 对插入的数据进行校验，如果发现数据长度或者类型不匹配
django


"""
MYSQL_OPTIONS={
    'sql_mode':'TRADITIONAL',
    'charset':'utf8',
    #mysql引擎
    'init_command':'SET default_storage=INNODB',
    'read_default_file':'config/db.cnf'
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '91pro',
        'HOST':'127.0.0.1',
        'PORT':'3306',
        'USER':'root',
        'PASSWORD':'970215',
        'CHARSET':'utf8'
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True
#是否使用Django时间
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static'),
    os.path.join(BASE_DIR,'apps/home/static'),
    os.path.join(BASE_DIR,'apps/account/static')
]

#当使用继承的方式重写auth模块的用户表的时候，
#需要指定一下
#app的名字，用户类名
AUTH_USER_MODEL='account.User'


#==============发送邮件配置=========
#发送邮件的服务器地址
EMAIL_HOST='smtp.163.com'
#发送邮件端口
EMAIL_PORT=25
#发送邮件默认的名称
EMAIL_HOST_USER='15570662291@163.com'
#授权码
EMAIL_HOST_PASSWORD='py1805'
#是否启用tls安全协议
EMAIL_URL_TLS=True

