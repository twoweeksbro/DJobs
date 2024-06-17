from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

from hello.models import Question
from hello.forms import UserCreateForm, UserLoginForm



bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_world():
    return 'Hello, World!'

@bp.route('/')
def index():
    form = UserLoginForm()

    return render_template('pages/landing.html',form=form)
# def index():
#    return redirect(url_for('question._list'))