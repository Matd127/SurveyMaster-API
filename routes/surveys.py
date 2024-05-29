from flask import Blueprint, jsonify
import datetime

surveys_bp = Blueprint('surveys', __name__)

surveys = [{'name': 'Good Idea', 'answer': 'Too big', 'dateOfCreate': datetime.datetime(2024, 12, 11)}]

@surveys_bp.route('/survey', methods=['GET'])
def get_surveys():
    return jsonify (surveys), 201

@surveys_bp.route('/survey', methods=["POST"])
def create_surveys(): 
    return jsonify({'message': 'success!'}), 200

@surveys_bp.route('/survey', methods=["PUT"])
def edit_survey(id): 
    return jsonify({'message': f'Updated survey: {id}'}), 200

@surveys_bp.route('/survey', methods=["DELETE"])
def edit_survey(id): 
    return jsonify({'message': f'Deleted survey: {id}'}), 200

