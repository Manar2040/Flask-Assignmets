from datetime import datetime
from ToDo import db, loginManager
from flask_login import UserMixin


@loginManager.user_loader
def load_user(userId):
    return User.query.get(int(userId))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    tasks = db.relationship("Task", backref="author", lazy=True)

    def __repr__(self):
        return f"User ( {self.name}, {self.email}, {self.image} )"


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Task ( {self.title}, {self.created_at} )"