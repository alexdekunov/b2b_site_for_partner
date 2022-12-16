from sqlalchemy import Column, Integer, String
from db import Base, engine


# Создаём новую модель т.е. питоновский класс
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)  # целое число и первичный ключ
    name = Column(String())
    salary = Column(Integer())
    email = Column(String(120), unique=True)  # колонка должна быть уникальной

    def __repr__(self):  # метод вызывается когда вызываем юзера в командной строке
        return f"User {self.id}, {self.name}"  # будем видеть его имя и айди когда вводим в командную строку

# новая таблица со статусами
class Partner_status(Base):
    __tablename__ = "partner_status"

    id = Column(Integer, primary_key=True)  # целое число и первичный ключ
    status = Column(String())

    def __repr__(self):  # метод вызывается когда вызываем юзера в командной строке
        return f"User {self.id}, {self.name}"  # будем видеть его имя и айди когда вводим в командную строку


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)  # создаст в нашей базе данных новую таблицу
