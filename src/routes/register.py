from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for
import sqlite3

from modules.init_db import *


register = Blueprint('register', __name__)


def get_db_connection():
    db = sqlite3.connect('data/database.db')
    db.row_factory = sqlite3.Row
    return db


@register.get('/')
def home():
    return render_template('register.html')


@register.post('/')
def register_user():
    print(request.get_data())
    return '1'
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cursor = get_db_connection()

    # Insert a row of data
    cursor.execute('INSERT INTO users VALUES (?, ?, ?, ?)',
                   (username, email, password, date))

    # Save (commit) the changes
    cursor.commit()

    # print all users
    print(cursor.execute('SELECT * FROM users').fetchall())

    return redirect(url_for('login.login'))
