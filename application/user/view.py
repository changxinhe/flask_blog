from flask import Blueprint

#添加用户蓝图，用户路由根目录为/user
user_blueprint = Blueprint('user',__name__,url_prefix='/user')