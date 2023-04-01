from flask import Blueprint, render_template
root = Blueprint('root', __name__)

@root.get('/')
def home():
    return render_template('index.html')