from models import User

user = User.query.first()
print(user)
print(f"""Имя {user.name}
Зарплата {user.salary}
email {user.email}""")

# мы видем потому что в models.py  есть def __repr__(self):
# если его убрать то мы будем видеть только <models.User object at 0x0000029BBE98F850> адрес объекта
