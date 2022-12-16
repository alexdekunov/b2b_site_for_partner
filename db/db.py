from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('postgresql://vsogutja:9EYEFeGVwqi_ieJIxfCrxDPeUVJVq5FC@mouse.db.elephantsql.com/vsogutja')
# ссылка из базы данных elephant
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

