from flask import Blueprint, render_template

blueprint = Blueprint('news', __name__)

@blueprint.route('/news')
def get_news():
    title = "Новости"
    return render_template('news/news.html', page_title=title)