from flask import Blueprint, request, jsonify, Response
from datetime import datetime
from models.survey import Survey
from bson import ObjectId
from bson.json_util import dumps
from config.db import db

surveys_bp = Blueprint('surveys', __name__)


@surveys_bp.route('/survey', methods=['GET'])
def get_surveys():
    surveys = db['surveys'].find()
    surveys_list = dumps(list(surveys))
    return Response(surveys_list, mimetype='application/json'), 200


@surveys_bp.route('/survey/<id>', methods=['GET'])
def get_survey(id):
    survey_id = ObjectId(id)
    survey = db['surveys'].find_one({'_id': survey_id})

    if survey:
        survey['_id'] = str(survey['_id'])
        return jsonify(survey), 200
    else:
        return jsonify({'error': 'Survey not found'}), 404


@surveys_bp.route('/survey', methods=['POST'])
def create_survey():
    try:
        data = request.get_json()
        data['start_date'] = datetime.strptime(data['start_date'], '%Y-%m-%d')
        data['end_date'] = datetime.strptime(data['end_date'], '%Y-%m-%d')
        data['owner'] = ObjectId(data['owner'])
        survey = Survey(**data)
        db['surveys'].insert_one(survey.dict(by_alias=True))
        return jsonify({"message": "Successfully created new survey"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@surveys_bp.route('/survey/<id>', methods=["PUT"])
def edit_survey(id):
    survey_id = ObjectId(id)
    survey = db['surveys'].find_one({'_id': survey_id})

    if survey:
        update_data = request.json
        result = db['surveys'].update_one(survey, {'$set': update_data})

        if result.modified_count == 1:
            return jsonify({'message': 'Survey updated successfully'}), 201
        else:
            return jsonify({'message': 'No changes applied to the survey'}), 200
    else:
        return jsonify({'error': 'Survey does not exist'}), 404


@surveys_bp.route('/survey/<id>', methods=['DELETE'])
def delete_survey(id):
    survey_id = ObjectId(id)
    result = db['surveys'].delete_one({'_id': survey_id})

    if result.deleted_count == 1:
        return jsonify({'message': 'Survey deleted successfully'}), 200
    else:
        return jsonify({'error': 'Survey not found'}), 404