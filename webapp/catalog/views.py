from flask import Blueprint, render_template

blueprint = Blueprint('catalog', __name__)


@blueprint.route('/catalog')
def about():
    title = "Каталог"
    return render_template('catalog/about.html', page_title=title)
    