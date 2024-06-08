from flask import Blueprint, request
from models.tag import Tag
from utils.crud_helpers import get_all, get_one, create_item, update_item, delete_item

tags_bp = Blueprint('tags', __name__)

@tags_bp.route('/tag', methods=['GET'])
def get_tags():
    return get_all('tags')

@tags_bp.route('/tag/<id>', methods=['GET'])
def get_tag(id):
    return get_one('tags', id)

@tags_bp.route('/tag', methods=['POST'])
def create_tag():
    data = request.get_json()
    tag = Tag(**data)
    return create_item('tags', tag.dict(by_alias=True))

@tags_bp.route('/tag/<id>', methods=['PUT'])
def edit_tag(id):
    update_data = request.json
    return update_item('tags', id, update_data)

@tags_bp.route('/tag/<id>', methods=['DELETE'])
def delete_tag(id):
    return delete_item('tags', id)
