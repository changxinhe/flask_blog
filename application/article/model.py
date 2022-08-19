from datetime import datetime

from application import db


class Article(db.Model):
    __tatlename__ = 'artile'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True,)
    title = db.Column(db.String(50),nullable=False)
    content = db.Column(db.Text,nullable=False)
    pdatime = db.Column(db.DateTime,default=datetime.now(),comment='创建时间')
    click_num = db.Column(db.Integer,default=0)
    save_num = db.Column(db.Integer,default=0)
    like_num = db.Column(db.Integer,default=0)
    use_id =db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)

