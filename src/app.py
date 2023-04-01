import os
from dotenv import load_dotenv
from flask import Flask
from routes.root import root
from routes.login import login

app = Flask(__name__, template_folder='./templates', static_folder='./static')

app.register_blueprint(root, url_prefix='/')
app.register_blueprint(login, url_prefix='/login')

if __name__ == '__main__':
    load_dotenv()
    app.run(
        host=os.getenv('HOST'),
        port=os.getenv('PORT'),
        debug=os.getenv('DEBUG')
    )
