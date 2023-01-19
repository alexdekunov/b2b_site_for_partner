from flask import Blueprint, render_template

blueprint = Blueprint('top', __name__)


@blueprint.route('/')
def index():
    title = "Главная страница"
    return render_template('index.html', page_title=title)