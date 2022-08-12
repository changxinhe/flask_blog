from flask import Flask
from application import config
from application.datasource import db, bootstrap


def create_app():
    app = Flask(__name__,
                static_folder='',
                template_folder=''
                )

    # 初始化配置文件
    app.config.from_object(config.DevelopmentConfig)

    # 初始化数据库
    db.init_app(app=app)
    # 初始化bootstrap
    bootstrap.init_app(app=app)

    # 注册视图函数
    app.register_blueprint()

    return app



