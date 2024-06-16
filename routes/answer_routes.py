from flask import Blueprint, request, jsonify
from models.answer import Answer
from utils.crud_helpers import get_all, get_one, create_item, update_item, delete_item

answers_bp = Blueprint('questions', __name__)


@answers_bp.route('/answers', methods=['GET'])
def get_all_answers():
    return get_all('answers')


@answers_bp.route('/answers/<id>', methods=['GET'])
def get_answer(id):
    return get_one('answers', id)


@answers_bp.route('/answers', methods=['POST'])
def create_answer():
    try:
        data = request.get_json()
        answer = Answer(**data)
        return create_item('answers', answer.dict(by_alias=True))
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@answers_bp.route('/answers/<id>', methods=['PUT'])
def update_answer(id):
    try:
        data = request.get_json()
        answer = Answer(**data)
        return update_item('answers', id, answer.dict(by_alias=True))
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@answers_bp.route('/answers/<id>', methods=['DELETE'])
def delete_answer(id):
    return delete_item('answers', id)
