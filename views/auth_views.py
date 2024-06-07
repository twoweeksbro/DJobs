from flask import Blueprint, url_for, render_template, flash, request
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect

from hello import db
from hello.forms import UserCreateForm
from hello.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(log_id=form.username.data).first()
        if not user:
            user = User(log_id=form.username.data,
                        password=generate_password_hash(form.password1.data),
                        car=form.car.data,
                        name=form.name.data,
                        email=form.email.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('이미 존재하는 아이디입니다.')
    return render_template('auth/signup.html', form=form)
