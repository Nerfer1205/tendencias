class Config(object):
    DEBUG=True

class ProductionConfig(Config):
    SECRET_KEY = '075102ad69bff65857ebfe8b03f0e1f54571cd724713c3710653496702ae6e9f'
    JWT_SECRET_KEY = ''
    MYSQL_HOST = ''
    MYSQL_BD = ''
    MYSQL_USER = ''
    MYSQL_PASS = ''

class DevelopmentConfig(Config):
    SECRET_KEY = '836f57bd4eb7cde5dd6aea4a0d30b14e81aa93c7675dea4067d42ed27ede51c2'
    JWT_SECRET_KEY = ''
    MYSQL_HOST = ''
    MYSQL_BD = ''
    MYSQL_USER = ''
    MYSQL_PASS = ''