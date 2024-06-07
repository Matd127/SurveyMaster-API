from flask import Blueprint, request, jsonify, Response
from models.user import User
from config.db import db
from bson.json_util import dumps
from bson import ObjectId

users_bp = Blueprint('users', __name__)


@users_bp.route('/user/<id>', methods=['GET'])
def get_user(id):
    user_id = ObjectId(id)
    user = db['users'].find_one({'_id': user_id})
    if user:
        user['_id'] = str(user['_id'])
        return jsonify(user), 200
    else:
        return jsonify({'error': 'User not found'}), 404


@users_bp.route('/user', methods=['GET'])
def get_users():
    users = db['users'].find()
    user_list = dumps(list(users))
    return Response(user_list, mimetype='application/json'), 200


@users_bp.route('/user', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        user = User(**data)
        collection = db['users']
        collection.insert_one(user.dict(by_alias=True))
        return jsonify({"message": "Successfully created new account!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@users_bp.route('/user/<id>', methods=['PUT'])
def update_user(id):
    user_id = ObjectId(id)
    user = db['users'].find_one({'_id': user_id})

    if user:
        update_data = request.json
        result = db['users'].update_one(user, {'$set': update_data})

        if result.modified_count == 1:
            return jsonify({'message': 'User updated successfully'}), 201
        else:
            return jsonify({'message': 'No changes applied to the user'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404


@users_bp.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        user_id = ObjectId(id)
    except Exception as e:
        return jsonify({'error': 'Invalid user ID format'}), 400

    result = db['users'].delete_one({'_id': user_id})

    if result.deleted_count == 1:
        return jsonify({'message': 'User deleted successfully'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404
