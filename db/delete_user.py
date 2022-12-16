from db import db_session
from models import Partner_status, User

# удаляем пользователя
user = User.query.first()
db_session.delete(user)
db_session.commit()

# удаляем статус в таблице статусов
status = Partner_status.query.first()
db_session.delete(status)
db_session.commit()

