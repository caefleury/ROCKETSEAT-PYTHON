from flask import Flask, request, jsonify
from database import db
from dotenv import load_dotenv
import os
from models.user import User
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/login", methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if username and password:
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return jsonify({"message": "Usuario logado com sucesso!"}), 200
    return jsonify({"message": "Credenciais invalidas"}), 400


@app.route("/logout", methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Usuário deslogado com sucesso"})


@app.route("/user", methods=["POST"])
def create_user():
    data = request.json
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if username and password and email:
        find_user_by_username = User.query.filter_by(username=username).first()
        find_user_by_email = User.query.filter_by(email=email).first()
        if find_user_by_username:
            return jsonify({"message": "Esse nome de usuário já existe"}), 400
        elif find_user_by_email:
            return jsonify({"message": "Esse email já está sendo utilizado por outro usuário"}), 400

        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "Usuário criado com sucesso"}), 200

    return jsonify({"message", "Dados inválidos"}), 400


if __name__ == '__main__':
    app.run(debug=True)
