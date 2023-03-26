from flask import Blueprint
root = Blueprint('root', __name__)

@root.get('/')
def home():
    return 'Hello World!'