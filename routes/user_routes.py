from flask import Blueprint, request
from models.user import User
from utils.crud_helpers import get_all, get_one, create_item, update_item, delete_item

users_bp = Blueprint('users', __name__)


@users_bp.route('/user', methods=['GET'])
def get_users():
    return get_all('users')


@users_bp.route('/user/<id>', methods=['GET'])
def get_user(id):
    return get_one('users', id)


@users_bp.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(**data)
    return create_item('users', user.dict(by_alias=True))


@users_bp.route('/user/<id>', methods=['PUT'])
def edit_user(id):
    update_data = request.json
    return update_item('users', id, update_data)


@users_bp.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    return delete_item('users', id)
