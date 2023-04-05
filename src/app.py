import os
from dotenv import load_dotenv
from flask import Flask
from routes.root import root
from routes.login import login
from routes.register import register

app = Flask(__name__, template_folder='./templates', static_folder='./static')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


app.register_blueprint(root, url_prefix='/')
app.register_blueprint(login, url_prefix='/login')
app.register_blueprint(register, url_prefix='/register')

if __name__ == '__main__':
    load_dotenv()
    app.run(
        host=os.getenv('HOST'),
        port=os.getenv('PORT'),
        debug=os.getenv('DEBUG')
    )
