from db import db_session
from models import User

# вводим данные пользователя
user = User(name="Petr", salary=23000, email='vlad@dsd.ru')
# что бы добавить надо создать сессию
db_session.add(user)
db_session.commit()

