import os
basedir = os.path.abspath(os.path.dirname(__file__))



class Config(object):
	DEBUG = False
	TESTING = False
	CSRF_ENABLED = True
	SECRET_KEY = '0af9719ffdef2aacb7a693ff3cd948bb769c86f6'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	SQLACHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(object):
	TESTING = True


class ProductionConfig(object):
	DEBUG = False


class DevelopmentConfig(object):
	TESTING = True
	DEBUG = True

class StagingConfig(object):
	TESTING = True
	DEBUG = True