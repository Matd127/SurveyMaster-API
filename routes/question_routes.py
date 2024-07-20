from flask import Blueprint, request, jsonify
from models.question import Question
from utils.crud_helpers import get_all, get_one, create_item, update_item, delete_item
from bson import ObjectId
from flask_jwt_extended import jwt_required

questions_bp = Blueprint('questions', __name__)


@questions_bp.route('/question', methods=['GET'])
def get_questions():
    return get_all('questions')

@questions_bp.route('/question/<id>', methods=['GET'])
def get_question(id):
    return get_one('questions', id)

@jwt_required()
@questions_bp.route('/question', methods=['POST'])
def create_question():
    try:
        data = request.get_json()
        data['survey'] = ObjectId(data['survey'])

        question = Question(**data)
        return create_item('questions', question.dict(by_alias=True))
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@jwt_required()
@questions_bp.route('/question/<id>', methods=['PUT'])
def edit_question(id):
    try:
        data = request.get_json()
        question = Question(**data)
        return update_item('questions', id, question.dict(by_alias=True))
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@jwt_required()
@questions_bp.route('/question/<id>', methods=['DELETE'])
def delete_question(id):
    return delete_item('questions', id)