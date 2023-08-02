from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Subscriber, db

subscriber_routes = Blueprint('subscribers', __name__)


@subscriber_routes.route('/')
@login_required
def subscribers():
    """
    Query for all subscribers and return them in a list of subscriber dictionaries
    """
    subscribers = Subscriber.query.all()
    return jsonify({'subscribers': [subscriber.to_dict() for subscriber in subscribers]})


@subscriber_routes.route('/<int:user_id>/<int:channel_id>', methods=['POST'])
@login_required
def subscribe(user_id, channel_id):
    """
    Subscribe a user to a channel
    """
    subscriber = Subscriber(user_id=user_id, channel_id=channel_id)
    db.session.add(subscriber)
    db.session.commit()
    return jsonify(subscriber.to_dict()), 201


@subscriber_routes.route('/<int:user_id>/<int:channel_id>', methods=['DELETE'])
@login_required
def unsubscribe(user_id, channel_id):
    """
    Unsubscribe a user from a channel
    """
    subscriber = Subscriber.query.filter_by(user_id=user_id, channel_id=channel_id).first()
    if subscriber:
        db.session.delete(subscriber)
        db.session.commit()
        return jsonify({'message': 'Unsubscribed successfully'})
    else:
        return jsonify({'error': 'Subscriber not found'}), 404
