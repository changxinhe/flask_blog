from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from application import create_app, db
#加载数据库表
from application.article.model import Article
from application.user.model import User


app = create_app()

manager = Manager(app=app)

#命令工具
migrate = Migrate(app=app,db=db)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()