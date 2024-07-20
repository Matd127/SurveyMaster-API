from flask import Blueprint, request, jsonify
from models.survey import Survey
from utils.crud_helpers import get_all, get_one, create_item, update_item, delete_item
from datetime import datetime
from bson import ObjectId
from flask_jwt_extended import jwt_required

surveys_bp = Blueprint('surveys', __name__)


@surveys_bp.route('/survey', methods=['GET'])
def get_surveys():
    return get_all('surveys')


@surveys_bp.route('/survey/<id>', methods=['GET'])
def get_survey(id):
    return get_one('surveys', id)

@jwt_required()
@surveys_bp.route('/survey', methods=['POST'])
def create_survey():
    try:
        data = request.get_json()
        data['start_date'] = datetime.strptime(data['start_date'], '%Y-%m-%d')
        data['end_date'] = datetime.strptime(data['end_date'], '%Y-%m-%d')
        data['owner'] = ObjectId(data['owner'])
        survey = Survey(**data)
        return create_item('surveys', survey.dict(by_alias=True))
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@jwt_required()
@surveys_bp.route('/survey/<id>', methods=["PUT"])
def edit_survey(id):
    update_data = request.json
    return update_item('surveys', id, update_data)

@jwt_required()
@surveys_bp.route('/survey/<id>', methods=['DELETE'])
def delete_survey(id):
    return delete_item('surveys', id)