from db import db_session
from models import Partner_status

status = Partner_status(status='autoris')

db_session.add(status)
db_session.commit()
