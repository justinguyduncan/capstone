from .db import db, environment, SCHEMA, add_prefix_for_prod
class Subscriber(db.Model):
    __tablename__ = 'subscribers'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('channels.id')), nullable=False)

    def __init__(self, user_id, channel_id):
        self.user_id = user_id
        self.channel_id = channel_id

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'channel_id': self.channel_id
        }
