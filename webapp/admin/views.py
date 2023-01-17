from flask import Blueprint
from flask_login import current_user, login_required

blueprint = Blueprint('admin', __name__, url_prefix='/admin')

@blueprint.route('/')
@login_required
def admin_index():
    if current_user.is_admin:
        return 'Привет админ!'
    else:
        return 'Ты не админ!'
