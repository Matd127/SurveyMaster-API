from flask import Blueprint, request
from models.user import User
from utils.crud_helpers import get_all, get_one, create_item, update_item, delete_item
from flask_jwt_extended import jwt_required

users_bp = Blueprint('users', __name__)

@jwt_required()
@users_bp.route('/user', methods=['GET'])
def get_users():
    return get_all('users')

@jwt_required()
@users_bp.route('/user/<id>', methods=['GET'])
def get_user(id):
    return get_one('users', id)

@jwt_required()
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
