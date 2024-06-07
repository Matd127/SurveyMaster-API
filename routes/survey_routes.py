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
    print(f"Survey ID: {id}")
    return jsonify({"survey_id": id}), 200


@surveys_bp.route('/survey', methods=['POST'])
def create_survey():
    try:
        data = request.get_json()
        data['start_date'] = datetime.strptime(data['start_date'], '%Y-%m-%d')
        data['end_date'] = datetime.strptime(data['end_date'], '%Y-%m-%d')
        data['owner'] = ObjectId(data['owner'])

        survey = Survey(**data)
        collection = db['surveys']
        collection.insert_one(survey.dict(by_alias=True))
        return jsonify({"message": "Successfully created new survey!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@surveys_bp.route('/survey', methods=["PUT"])
def edit_survey(id):
    return jsonify({'message': f'Updated survey: {id}'}), 200


@surveys_bp.route('/survey', methods=["DELETE"])
def delete_survey(id):
    return jsonify({'message': f'Deleted survey: {id}'}), 200
