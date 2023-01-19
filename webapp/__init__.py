from flask import Flask, render_template
from flask_login import LoginManager


from webapp.model import db
from webapp.user.models import User
from webapp.user.views import blueprint as user_blueprint
from webapp.admin.views import blueprint as admin_blueprint
from webapp.about.views import blueprint as about_blueprint
from webapp.top.views import blueprint as top_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(about_blueprint)
    app.register_blueprint(top_blueprint)


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
  
    return app
