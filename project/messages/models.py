from project import db
from datetime import datetime
# from project.users.models import User

Likes = db.Table('likes',
        db.Column('id',
                db.Integer,
                primary_key=True),
        db.Column('user_id',
                db.Integer,
                db.ForeignKey('users.id', ondelete="cascade")),
        db.Column('message_id',
                db.Integer,
                db.ForeignKey('messages.id', ondelete="cascade")),
        db.UniqueConstraint('user_id', 'message_id', name="one_time_like")
        )

class Message(db.Model):

    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
    user_likes = db.relationship('User',
        secondary=Likes,
        backref=db.backref('message_likes'))

    def __init__(self, text, user_id, timestamp=datetime.utcnow()):
        self.text = text
        self.user_id = user_id
        self.timestamp = timestamp
