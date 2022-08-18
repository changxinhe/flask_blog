import hashlib

from flask import Blueprint, render_template, request
from application import db
from application.user.model import User
from application.user.tool import encrypt

user_blueprint = Blueprint('user',__name__,url_prefix='/user/')
#添加用户蓝图，用户路由根目录为/user

@user_blueprint.route('/login', methods =['GET','POST'])
def root():
    if request.method == 'GET':
        return render_template('user/login.html')

@user_blueprint.route('/register', methods =['GET','POST'])
def register():
    if request.method == 'POST':
        if request.form.get('password') == request.form.get('repassword'):
            db.create_all()
            newuser = User()
            newuser.username = request.form.get('username')
            newuser.password = encrypt(request.form.get('password'))
            newuser.phone = request.form.get('phone')
            db.session.add(newuser)
            db.session.commit()
            return '注册成功'
        else:
            return '密码不一致'
    else:
        return render_template('user/register.html')


























# @user_blueprint.route('/register', methods =['GET','POST'])
# def register():
#     if request.method == 'POST':
#         if request.form.get('password') ==request.form.get('repassword'):
#             db.create_all()
#             # newuser = User
#             pass
#
#         pass