from db import db_session
from models import User

user = User.query.first()
# класс запрос первый
user.salary = 48800
# меняем ему зарплату
user.name = 'Boris'
db_session.commit()
# после этой сессии в базе поменяется значение

