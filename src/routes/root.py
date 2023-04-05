from flask import Blueprint, render_template
root_route = Blueprint('root_route', __name__)


@root_route.get('/')
def home():
    return render_template('index.html')
