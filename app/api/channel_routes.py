from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, Channel

channel_routes = Blueprint('channels', __name__)

# Route to get all channels for a user
@channel_routes.route('/', methods=['GET'])
@login_required
def get_user_channels():
    channels = Channel.query.filter_by(user_id=current_user.id).all()
    return {'channels': [channel.to_dict() for channel in channels]}

# Route to create a new channel for a user
@channel_routes.route('/', methods=['POST'])
@login_required
def create_channel():
    data = request.json
    title = data.get('title')
    description = data.get('description')

    if not title or not description:
        return jsonify({'error': 'Title and description are required'}), 400

    new_channel = Channel(user_id=current_user.id, title=title, description=description)
    db.session.add(new_channel)
    db.session.commit()

    return new_channel.to_dict(), 201

# Route to get a specific channel by ID
@channel_routes.route('/<int:channel_id>', methods=['GET'])
@login_required
def get_channel(channel_id):
    channel = Channel.query.get(channel_id)

    if not channel:
        return jsonify({'error': 'Channel not found'}), 404

    return channel.to_dict()

# Route to update an existing channel
@channel_routes.route('/<int:channel_id>', methods=['PUT'])
@login_required
def update_channel(channel_id):
    channel = Channel.query.get(channel_id)

    if not channel:
        return jsonify({'error': 'Channel not found'}), 404

    if channel.user_id != current_user.id:
        return jsonify({'error': 'You are not authorized to update this channel'}), 403

    data = request.json
    title = data.get('title')
    description = data.get('description')

    if not title or not description:
        return jsonify({'error': 'Title and description are required'}), 400

    channel.title = title
    channel.description = description
    db.session.commit()

    return channel.to_dict()

# Route to delete an existing channel
@channel_routes.route('/<int:channel_id>', methods=['DELETE'])
@login_required
def delete_channel(channel_id):
    channel = Channel.query.get(channel_id)

    if not channel:
        return jsonify({'error': 'Channel not found'}), 404

    if channel.user_id != current_user.id:
        return jsonify({'error': 'You are not authorized to delete this channel'}), 403

    db.session.delete(channel)
    db.session.commit()

    return jsonify({'message': 'Channel deleted successfully'}), 200
