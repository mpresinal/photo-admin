from .base import *

# To activate this config the following enviroment variable must be set:
# PYTHON_ENV=PROD

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kq9y8)e$+7@(m3jp8=h=3pz+l3$-g)ccv_on%(7q$f@#%q+0ck'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'photoadmin',
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': 'postgres',
        'PASSWORD': 'postgres'
    },
}