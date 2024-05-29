from flask import Flask, jsonify
from routes.surveys import surveys_bp

app = Flask(__name__)
app.register_blueprint(surveys_bp)

@app.route('/')
def home():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run(port=5000)
