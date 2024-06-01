from flask import Blueprint, request, jsonify
import datetime
from models.survey import Survey

surveys_bp = Blueprint('surveys', __name__)
surveys = [
    Survey(
        title="Customer Feedback Survey",
        description="Please provide feedback on your recent experience with our services.",
        start_date=datetime.datetime(2024, 6, 1),
        end_date=datetime.datetime(2024, 6, 30),
        is_open=True,
        owner="123daw",
    )
]


@surveys_bp.route('/survey', methods=['GET'])
def get_surveys():
    survey_list = [survey.__dict__ for survey in surveys]
    return jsonify(survey_list), 200


@surveys_bp.route('/survey/:id', methods=['GET'])
def get_survey():
    survey_list = [survey.__dict__ for survey in surveys]
    return jsonify(survey_list), 200


@surveys_bp.route('/survey', methods=["POST"])
def create_survey():
    data = request.json
    try:
        start_date = datetime.strptime(data['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(data['end_date'], '%Y-%m-%d')

        new_survey = Survey(
            name=data['title'],
            description=data['description'],
            start_date=start_date,
            end_date=end_date,
            is_open=data['is_open']
        )
        surveys.append(new_survey)
        return jsonify({'message': 'Successfully created new survey!'}), 201
    except:
        return jsonify({'message': 'An error occured!'}), 400


@surveys_bp.route('/survey', methods=["PUT"])
def edit_survey(id):
    return jsonify({'message': f'Updated survey: {id}'}), 200


@surveys_bp.route('/survey', methods=["DELETE"])
def delete_survey(id):
    return jsonify({'message': f'Deleted survey: {id}'}), 200
