class  Config:
    DEBUG = True
    static_folder = 'D:\\python_project\\flask_blog\\static'
    template_folder = 'D:\\python_project\\flask_blog\\templates'
    #mysql数据源s
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:vvZh0DYi@47.110.161.170:3306/flask_blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    #SQLALCHEMY_COMMIT_ON_TEARDOWN = True #每次请求结束后都会自动提交数据库中变动sss

class DevelopmentConfig(Config):
    ENV = 'development'


class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
    