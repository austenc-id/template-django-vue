import os

SECRET_KEY = os.getenv('SECRET_KEY', default='django-devkey')

ROOT_URLCONF = 'config.urls'

DEBUG = True

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['127.0.0.1']

WSGI_APPLICATION = 'config.wsgi.application'
