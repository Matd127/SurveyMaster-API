from flask import Blueprint, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from config.db import db
from models.user import User
import bcrypt

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = db['users'].find_one({'username': username})
    
    if user:
        if bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify(error='Invalid login or password'), 401
    else:
        return jsonify(error='Invalid login or password'), 401 

@auth_bp.route('/register', methods=['POST'])
def register():
    data_from_request = request.get_json()
    user = User(**data_from_request)
    
    if db['users'].find_one({'username': user.username}):
        return jsonify(error='User already exists'), 400
    else:
        password = user.password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user.password = hashed_password.decode('utf-8')  
        db['users'].insert_one(user.dict(by_alias=True))
        return jsonify(message='User registered successfully'), 200

@auth_bp.route('/logout', methods=['POST'])

@jwt_required() 
def logout():
    return jsonify(message='Logged out successfully'), 200