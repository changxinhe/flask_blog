import hashlib

from flask import Blueprint, render_template, request, redirect, url_for
from application import db, user
from application.user.model import User
from application.user.tool import encrypt

user_blueprint = Blueprint('user',__name__,url_prefix='/user/')
#添加用户蓝图，用户路由根目录为/user

@user_blueprint.route('/login', methods =['GET','POST'])
def root():
    if request.method == 'GET':
        return render_template('user/login.html')

#用户注册
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
            return redirect(url_for('user.show'))
        else:
            return '密码不一致'
    else:
        return render_template('user/register.html')


#用户信息展示
@user_blueprint.route('/show',methods = ['GET','POST'])
def show():
    users = User.query.filter(User.isdelete==0).all()
    return render_template('user/show.html',users=users)

#用户修改
@user_blueprint.route('/user_update',methods=['POST','GET'])
def user_update():
    if request.method == 'POST':
        #定位用户
        user = User.query.get(request.form.get('id'))
        user.id = request.form.get('id')
        user.show_name = request.form.get('show_name')
        user.phone = request.form.get('phone')
        #数据库提交修改
        db.session.commit()
        return redirect(url_for('user.show'))

        pass
    else:
        id = request.args.get('id')
        user = User.query.get(id)
        return render_template('user/update.html',user=user)

#用户删除
@user_blueprint.route('/user_del',methods=['POST','GET'])
def user_del():
    if request.method == 'GET':
        #定位用户
        user = User.query.get(request.args.get('id'))
        #逻辑删除
        user.isdelete = 1
        db.session.commit()
        return redirect(url_for('user.show'))






















# @user_blueprint.route('/register', methods =['GET','POST'])
# def register():
#     if request.method == 'POST':
#         if request.form.get('password') ==request.form.get('repassword'):
#             db.create_all()
#             # newuser = User
#             pass
#
#         pass