import os
from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True,  nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(70), nullable=False)

    def _repr__(self):
        return f"User ('{self.username}', '{self.email}')"


class Developers(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    langueges = db.Column(db.String, nullable=False)
    level = db.Column(db.String, nullable=False)
    info = db.Column(db.String, nullable=False)


class Languege(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    langueges_list = db.Column(db.String, nullable=False)


class Levels(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    level_list = db.Column(db.String, nullable=False)