from flask import Blueprint, render_template

blueprint = Blueprint('about', __name__)


@blueprint.route('/about')
def about():
    title = "О нас"
    return render_template('about.html', page_title=title)