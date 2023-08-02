from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, User

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def get_users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def get_user_by_id(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = User.query.get(id)
    return user.to_dict()


@user_routes.route('/update', methods=['PUT'])
@login_required
def update_user():
    """
    Update the current user's profile information
    """
    data = request.get_json()
    user = current_user

    if 'username' in data:
        user.username = data['username']

    if 'email' in data:
        user.email = data['email']

    if 'image_url' in data:
        user.image_url = data['image_url']

    if 'password' in data:
        user.password = data['password']  # Automatically hashed due to property setter

    db.session.commit()
    return user.to_dict()


@user_routes.route('/delete', methods=['DELETE'])
@login_required
def delete_user():
    """
    Delete the current user's account
    """
    user = current_user
    db.session.delete(user)
    db.session.commit()
    return {'message': 'Account deleted successfully'}


@user_routes.route('/status')
def auth_status():
    """
    Check the current user's authentication status
    """
    if current_user.is_authenticated:
        return {'message': 'You are logged in'}
    else:
        return {'message': 'You are logged out'}


# Add other routes based on your application's requirements
# ...

