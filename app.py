from flask import Flask, jsonify
from routes.survey_routes import surveys_bp
from routes.user_routes import users_bp
from routes.auth_routes import auth_bp
from routes.tag_routes import tags_bp
from routes.question_routes import questions_bp
from routes.answer_routes import answers_bp

app = Flask(__name__)
app.register_blueprint(surveys_bp)
app.register_blueprint(users_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(tags_bp)
app.register_blueprint(questions_bp)
app.register_blueprint(answers_bp)


@app.route('/')
def home():
    return jsonify({'message': 'Hello, World!'}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
