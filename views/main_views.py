from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_world():
    return 'Hello, World!'

@bp.route('/')
def index():
    return 'Pybo index'