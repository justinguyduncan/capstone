from datetime import datetime
from .db import db, environment, SCHEMA, add_prefix_for_prod

class VOD(db.Model):
    __tablename__ = 'vods'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    channel_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('channels.id')), nullable=False)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    upload_time = db.Column(db.DateTime, default=datetime.utcnow)
    video_url = db.Column(db.String(255))

    channel = db.relationship('Channel', back_populates='vods')
    comments = db.relationship('Comment', back_populates='vod')
    def to_dict(self):
        return {
            'id': self.id,
            'channel_id': self.channel_id,
            'title': self.title,
            'description': self.description,
            'tags': self.tags,
            'upload_time': self.upload_time,
            'video_url': self.video_url
        }
