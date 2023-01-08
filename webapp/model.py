from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# модель описывает объект который будем класть в бд и брать из бд

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    published = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=True)
    
    def __repr__(self):
        return '<News {} {}>'.format(self.title, self.published)