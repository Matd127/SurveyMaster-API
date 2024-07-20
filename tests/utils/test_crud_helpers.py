import pytest
from unittest.mock import MagicMock, patch
from flask import Flask, jsonify, request
from bson import ObjectId
from utils.crud_helpers import get_all, get_one, create_item, update_item, delete_item

@pytest.fixture
def app():
    app = Flask(__name__)

    @app.route('/items', methods=['GET'])
    def get_items():
        return get_all('items')

    @app.route('/items/<id>', methods=['GET'])
    def get_single_item(id):
        return get_one('items', id)

    @app.route('/items', methods=['POST'])
    def create_new_item():
        data = request.json
        return create_item('items', data)

    @app.route('/items/<id>', methods=['PUT'])
    def update_existing_item(id):
        data = request.json
        return update_item('items', id, data)

    @app.route('/items/<id>', methods=['DELETE'])
    def delete_existing_item(id):
        return delete_item('items', id)

    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_one_valid_id(client):
    mock_db = MagicMock()
    with patch('utils.crud_helpers.db', mock_db):
        mock_db['items'].find_one.return_value = {'_id': ObjectId('60d0fe4f5311236168a109ca'), 'name': 'Test Item'}
        response = client.get('/items/60d0fe4f5311236168a109ca')
        assert response.status_code == 200
        assert response.json == {'_id': '60d0fe4f5311236168a109ca', 'name': 'Test Item'}

def test_update_item(client):
    mock_db = MagicMock()
    with patch('utils.crud_helpers.db', mock_db):
        mock_db['items'].find_one.return_value = {'_id': ObjectId('60d0fe4f5311236168a109ca'), 'name': 'Old Item'}
        mock_db['items'].update_one.return_value.modified_count = 1
        response = client.put('/items/60d0fe4f5311236168a109ca', json={'name': 'Updated Item'})
        assert response.status_code == 200
        assert response.json == {'message': 'Updated successfully'}

def test_delete_item(client):
    mock_db = MagicMock()
    with patch('utils.crud_helpers.db', mock_db):
        mock_db['items'].delete_one.return_value.deleted_count = 1
        response = client.delete('/items/60d0fe4f5311236168a109ca')
        assert response.status_code == 200
        assert response.json == {'message': 'Deleted successfully'}
