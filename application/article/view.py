from flask import Blueprint

#添加文章蓝图，文章路由根目录为/article
article_blueprint = Blueprint('article',__name__,url_prefix='/artilce')