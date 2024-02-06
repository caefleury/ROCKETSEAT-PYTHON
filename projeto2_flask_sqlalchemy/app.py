from flask import Flask, request, jsonify
from database import db
from dotenv import load_dotenv
import os
from models.user import User

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


db.init_app(app)


@app.route('/users', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})


if __name__ == '__main__':
    app.run(debug=True)
