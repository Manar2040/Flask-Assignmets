
from extensions import db
from datetime import datetime

class Tasks (db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    title=db.Column(db.String(50),nullable=False)
    completed=db.Column(db.Boolean,default=False)

    def __repr__(self):
        return '<Task %r>' % self.title


