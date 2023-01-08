from flask import Flask, render_template

from webapp.model import db


def create_app():
    app = Flask(__name__)
    #app.config.from_pyfile('config.py')
    #db.init_app(app)

    @app.route('/')
    def index():
        title = "Новый проект"
        return render_template('index.html')

    return app