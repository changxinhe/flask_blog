from flask import Flask
from application import config
from application.article.view import article_blueprint
from application.datasource import db, bootstrap
from application.user.view import user_blueprint


def create_app():
    app = Flask(__name__,template_folder = 'templates')

    # 初始化配置文件
    app.config.from_object(config.DevelopmentConfig)

    # 初始化数据库
    db.init_app(app=app)
    # 初始化bootstrap
    bootstrap.init_app(app=app)

    # 注册视图函数
    app.register_blueprint(user_blueprint)
    app.register_blueprint(article_blueprint)
    return app



