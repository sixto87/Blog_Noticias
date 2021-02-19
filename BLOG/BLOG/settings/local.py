from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME':'blog',
        'Trusted_Connection':'yes',
        'HOST': 'localhost\wincc',
        'OPTIONS':{
        	'driver':'SQL Server Native Client 11.0',
        }
    },
}
