from flask import Blueprint, render_template
login_route = Blueprint('login_route', __name__)

@login_route.get('/')
def login():
    return render_template('login.html')