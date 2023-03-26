from flask import Flask
from routes.root import root

app = Flask(__name__, template_folder='./templates', static_folder='./static')

app.register_blueprint(root, url_prefix='/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)