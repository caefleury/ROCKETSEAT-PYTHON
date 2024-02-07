from flask import Flask, request, jsonify
from database import db
from dotenv import load_dotenv
import os
from models.user import User
from flask_login import LoginManager

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

@app.route("/login", methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if username and password:
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            return jsonify({"message": "Usuario logado com sucesso!"}), 200
    return jsonify({"message": "Credenciais invalidas"}), 400


@app.route('/users', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})


if __name__ == '__main__':
    app.run(debug=True)
