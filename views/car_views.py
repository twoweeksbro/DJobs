from flask import Blueprint, render_template,url_for

from hello.models import Charge
bp = Blueprint('car', __name__, url_prefix='/car')

@bp.route('/charging')
def charging_page():
    return render_template('pages/charging.html')

@bp.route('/mypage')
def my_page():
    return render_template('pages/mypage.html')