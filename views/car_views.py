from flask import Blueprint, render_template,url_for, request, jsonify

from datetime import datetime
from werkzeug.utils import redirect

from hello.models import Charge
from hello import db

bp = Blueprint('car', __name__, url_prefix='/car')

@bp.route('/charging/', methods=('GET','POST'))
def charging_page():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        parking = data.get('parking')
        position = data.get('position')
        model = data.get('model')

        cnt = Charge.query.count()
        minn = 5*cnt

        cha = Charge(name=minn,parking=parking,position=position,create_date=datetime.now(),expected_time=minn)


        db.session.add(cha)
        db.session.commit()
        print(f"성공 Received name: {name}, parking: {parking}, position: {position}, model: {model}")
        return redirect(url_for('main.index'))

    return render_template('pages/charging.html')

@bp.route('/mypage')
def my_page():
    return render_template('pages/mypage.html')
@bp.route('/submit', methods=['POST','GET'])
def submit():
    data = request.get_json()
    name = data.get('name')
    parking = data.get('parking')
    position = data.get('position')
    model = data.get('model')
    print(f"Received name: {name}, parking: {parking}, position: {position}, model: {model}")
    return jsonify({'name':name,'parking':parking,'position':position,'model':model })