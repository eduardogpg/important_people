import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_custome_secret_key'

class DevelopmentConfig(Config):
	DEBUG = True
	PORT = 8000