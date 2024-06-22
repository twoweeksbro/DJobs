from flask import Blueprint, render_template, flash, url_for, request, session, g

from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash,check_password_hash

from hello.models import Question, User
from hello.forms import UserCreateForm, UserLoginForm



bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_world():
    return 'Hello, World!'

@bp.route('/', methods=('GET','POST'))
def index():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(log_id=form.username.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.index'))
        flash(error)
    return render_template('pages/landing.html', form=form)
# def index():
#    return redirect(url_for('question._list'))