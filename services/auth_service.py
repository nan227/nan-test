from models.user import User
from flask import session

class AuthService:
    @staticmethod
    def login(username, password):
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            session['user_id'] = user.id
            session['role'] = user.role
            return True
        return False

    @staticmethod
    def logout():
        session.clear()