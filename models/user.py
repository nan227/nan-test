from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'admin' or 'member'

class Member(db.Model):  # Extending user for members
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    issued_books = db.relationship('IssuedBook', backref='member', lazy=True)