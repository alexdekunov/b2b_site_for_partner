from flask import Flask, render_template

from webapp.forms import LoginForm


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        title = "Новый проект"
        return render_template('index.html')
    

    @app.route('/login')
    def login():
        title = 'Авторизация'
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    

    @app.route('/about')
    def about():
        title = "О нас"
        return render_template('about.html')

    return app