from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Comment, VOD, db

comment_routes = Blueprint('comments', __name__)


@comment_routes.route('/')
@login_required
def comments():
    """
    Query for all comments and return them in a list of comment dictionaries
    """
    comments = Comment.query.all()
    return jsonify({'comments': [comment.to_dict() for comment in comments]})


@comment_routes.route('/<int:vod_id>', methods=['POST'])
@login_required
def create_comment(vod_id):
    """
    Create a new comment on a VOD
    """
    data = request.get_json()
    content = data.get('content', '')

    vod = VOD.query.get(vod_id)
    if not vod:
        return jsonify({'error': 'VOD not found'}), 404

    comment = Comment(vod_id=vod_id, user_id=current_user.id, content=content)
    db.session.add(comment)
    db.session.commit()
    return jsonify(comment.to_dict()), 201


@comment_routes.route('/<int:comment_id>', methods=['PUT'])
@login_required
def update_comment(comment_id):
    """
    Update an existing comment
    """
    comment = Comment.query.filter_by(id=comment_id, user_id=current_user.id).first()
    if not comment:
        return jsonify({'error': 'Comment not found or you do not have permission to update it'}), 404

    data = request.get_json()
    content = data.get('content', '')

    comment.content = content
    comment.updated_at = datetime.utcnow()
    db.session.commit()
    return jsonify(comment.to_dict())


@comment_routes.route('/<int:comment_id>', methods=['DELETE'])
@login_required
def delete_comment(comment_id):
    """
    Delete a comment
    """
    comment = Comment.query.filter_by(id=comment_id, user_id=current_user.id).first()
    if not comment:
        return jsonify({'error': 'Comment not found or you do not have permission to delete it'}), 404

    db.session.delete(comment)
    db.session.commit()
    return jsonify({'message': 'Comment deleted successfully'})
