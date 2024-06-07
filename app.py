from flask import Flask, jsonify
from routes.survey_routes import surveys_bp
from routes.user_routes import users_bp
from routes.auth_routes import auth_bp

app = Flask(__name__)
app.register_blueprint(surveys_bp)
app.register_blueprint(users_bp)
app.register_blueprint(auth_bp)


@app.route('/')
def home():
    return jsonify({'message': 'Hello, World!'}), 200


if __name__ == '__main__':
    app.run(port=5000)
