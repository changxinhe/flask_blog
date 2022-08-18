from datetime import datetime

from application import db


class User(db.Model):
    __tablename__ = 'users'
    id =db.Column(db.Integer,primary_key=True,autoincrement=True)
    show_name = db.Column(db.String(15),default='用户X',comment='用户名,显示名称')
    username =db.Column(db.String(15),unique=True,nullable=False,comment='用户名，注册登录账号')
    password = db.Column(db.String(64),nullable=False,comment='用户登录密码')
    phone = db.Column(db.String(12),nullable=False,unique=True,comment='手机号码')
    email = db.Column(db.String(30),comment='邮箱')
    icon = db.Column(db.String(100))
    rdtime = db.Column(db.DateTime,default=datetime.now(),comment='创建时间')
    isdelete =db.Column(db.Boolean,default=0,comment='用户状态,1：删除,0：存在')
