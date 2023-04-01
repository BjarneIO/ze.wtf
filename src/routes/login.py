from flask import Blueprint, render_template
login = Blueprint('login', __name__)

@login.get('/')
def home():
    return render_template('login.html')