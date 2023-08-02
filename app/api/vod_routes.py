from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import VOD, db

vod_routes = Blueprint('vods', __name__)


@vod_routes.route('/')
@login_required
def vods():
    """
    Query for all VODs and return them in a list of VOD dictionaries
    """
    vods = VOD.query.all()
    return jsonify({'vods': [vod.to_dict() for vod in vods]})


@vod_routes.route('/<int:id>')
@login_required
def vod(id):
    """
    Query for a VOD by id and return that VOD in a dictionary
    """
    vod = VOD.query.get(id)
    if vod:
        return jsonify(vod.to_dict())
    else:
        return jsonify({'error': 'VOD not found'}), 404


@vod_routes.route('/', methods=['POST'])
@login_required
def create_vod():
    """
    Create a new VOD and add it to the database
    """
    data = request.get_json()
    vod = VOD(
        channel_id=data['channel_id'],
        title=data['title'],
        description=data['description'],
        tags=data['tags'],
        video_url=data['video_url']
    )
    db.session.add(vod)
    db.session.commit()
    return jsonify(vod.to_dict()), 201


@vod_routes.route('/<int:id>', methods=['PUT'])
@login_required
def update_vod(id):
    """
    Update an existing VOD
    """
    vod = VOD.query.get(id)
    if vod:
        data = request.get_json()
        vod.title = data['title']
        vod.description = data['description']
        vod.tags = data['tags']
        vod.video_url = data['video_url']
        db.session.commit()
        return jsonify(vod.to_dict())
    else:
        return jsonify({'error': 'VOD not found'}), 404


@vod_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_vod(id):
    """
    Delete an existing VOD
    """
    vod = VOD.query.get(id)
    if vod:
        db.session.delete(vod)
        db.session.commit()
        return jsonify({'message': 'VOD deleted successfully'})
    else:
        return jsonify({'error': 'VOD not found'}), 404

