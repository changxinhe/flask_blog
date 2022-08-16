from flask import Blueprint, render_template, request

#添加用户蓝图，用户路由根目录为/user
from application import db

user_blueprint = Blueprint('user',__name__,url_prefix='/user/')

@user_blueprint.route('/login', methods =['GET','POST'])
def root():
    if request.method == 'GET':
        return render_template('user/login.html')


@user_blueprint.route('/register', methods =['GET','POST'])
def register():
    if request.method == 'POST':
        if request.form.get('password') ==request.form.get('repassword'):
            db.create_all()
            newuser = User


        pass