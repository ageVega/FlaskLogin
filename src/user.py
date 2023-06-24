#user.py
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, nickname, password):
        self.id = id
        self.nickname = nickname
        self.password = password
