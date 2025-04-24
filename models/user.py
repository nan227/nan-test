from datetime import datetime

class User:
    def __init__(self, user_id, username, password, role):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role
        self.borrowed_books = []

class Admin(User):
    def __init__(self, user_id, username, password):
        super().__init__(user_id, username, password, role='admin')

class Member(User):
    def __init__(self, user_id, username, password):
        super().__init__(user_id, username, password, role='member')
