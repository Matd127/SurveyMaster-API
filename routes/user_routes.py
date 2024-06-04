from flask import Blueprint, request, jsonify
from models.user import User
from bson import ObjectId
from config.db import db

users_bp = Blueprint('users', __name__)

@users_bp.route('/user', methods=['GET'])
def get_users():
    users_list = [users.__dict__ for users in users]
    return jsonify(users_list), 200


@users_bp.route('/user', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        user = User(**data)
        collection = db['users']
        result = collection.insert_one(user.dict(by_alias=True))
        return jsonify({"inserted_id": str(result.inserted_id)}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
