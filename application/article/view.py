from flask import Blueprint, request, render_template

from application.datasource import db
from application.article.model import Article
from application.user.model import User

#添加文章蓝图，文章路由根目录为/article
article_blueprint = Blueprint('article',__name__,url_prefix='/article')

@article_blueprint.route('/push', methods=['GET','POST'])
def push():
    if request.method == 'POST':
        new_article = Article()
        new_article.title = request.form.get('title')
        new_article.content = request.form.get('content')
        new_article.user_id = request.form.get('uid')
        db.session.add(new_article)
        db.session.commit()
        return '添加成功'
    else:
        users = User.query.filter_by(isdelete=0).all()
        return render_template('article/add_article.html',users=users)
