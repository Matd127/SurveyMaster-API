from flask import request, jsonify, Response
from bson.json_util import dumps
from bson import ObjectId
from config.db import db


def get_all(collection_name):
    id = request.args.get('id')
    if id:
        try:
            items = db[collection_name].find({"_id": ObjectId(id)})
        except Exception as e:
            return Response({"error": str(e)}, mimetype='application/json'), 400
    else:
        items = db[collection_name].find()

    items_list = dumps(list(items))
    return Response(items_list, mimetype='application/json'), 200


def get_one(collection_name, id):
    try:
        item_id = ObjectId(id)
    except Exception:
        return jsonify({'error': 'Invalid ID format'}), 400

    item = db[collection_name].find_one({'_id': item_id})
    if item:
        item['_id'] = str(item['_id'])
        return jsonify(item), 200
    else:
        return jsonify({'error': f'{collection_name[:-1].capitalize()} not found'}), 404


def create_item(collection_name, data):
    try:
        collection = db[collection_name]
        collection.insert_one(data)
        return jsonify({"message": "Successfully created"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


def update_item(collection_name, id, update_data):
    try:
        item_id = ObjectId(id)
    except Exception:
        return jsonify({'error': 'Invalid ID format'}), 400

    item = db[collection_name].find_one({'_id': item_id})
    if item:
        result = db[collection_name].update_one(
            {'_id': item_id}, {'$set': update_data})
        if result.modified_count == 1:
            return jsonify({'message': 'Updated successfully'}), 200
        else:
            return jsonify({'message': 'No changes applied'}), 200
    else:
        return jsonify({'error': f'{collection_name[:-1].capitalize()} not found'}), 404


def delete_item(collection_name, id):
    try:
        item_id = ObjectId(id)
    except Exception:
        return jsonify({'error': 'Invalid ID format'}), 400

    result = db[collection_name].delete_one({'_id': item_id})
    if result.deleted_count == 1:
        return jsonify({'message': 'Deleted successfully'}), 200
    else:
        return jsonify({'error': f'{collection_name[:-1].capitalize()} not found'}), 404
