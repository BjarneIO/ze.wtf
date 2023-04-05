from flask import Blueprint, render_template
register_route = Blueprint('register_route', __name__)

@register_route.get('/')
def register():
    return render_template('register.html')

