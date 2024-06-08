from flask import Blueprint, request, jsonify, Response
from datetime import datetime
from models.tag import Tag
from bson import ObjectId
from bson.json_util import dumps
from config.db import db

tags_bp = Blueprint('tags', __name__)


@tags_bp.route('/tag', methods=['GET'])
def get_tags():
    tags = db['tags'].find()
    tags_list = dumps(list(tags))
    return Response(tags_list,  mimetype='application/json'), 200


@tags_bp.route('/tag', methods=['POST'])
def create_tag():
    try:
        data = request.get_json()
        tag = Tag(**data)
        db['tags'].insert_one(tag.dict(by_alias=True))
        return jsonify({"message": "Successfully created new tag"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@tags_bp.route('/tag/<id>', methods=['PUT'])
def edit_tag(id):
    tag_id = ObjectId(id)
    tag = db['tags'].find_one({'_id': tag_id})

    if tag:
        update_data = request.json
        result = db['tags'].update_one(tag, {'$set': update_data})

        if result.modified_count == 1:
            return jsonify({'message': 'Tag updated successfully'}), 201
        else:
            return jsonify({'message': 'No changes applied to the tag'}), 200
    else:
        return jsonify({'error': 'Tag does not exist'}), 404


@tags_bp.route('/tag/<id>', methods=['DELETE'])
def delete_tag(id):
    tag_id = ObjectId(id)
    result = db['tags'].delete_one({'_id': tag_id})

    if result.deleted_count == 1:
        return jsonify({'message': 'Tag deleted successfully'}), 200
    else:
        return jsonify({'error': 'Tag not found'}), 404
