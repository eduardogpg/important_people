import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_custome_secret_key'

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/important_people'
	SQLALCHEMY_TRACK_MODIFICATIONS = False

