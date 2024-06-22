from flask import Blueprint, render_template,url_for, request, jsonify, session, g

from datetime import datetime
from werkzeug.utils import redirect

from hello.models import Charge
from hello import db
from views.auth_views import login_required


bp = Blueprint('car', __name__, url_prefix='/car')

@bp.route('/charging/', methods=('GET','POST'))
@login_required
def charging_page():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        parking = data.get('parking')
        position = data.get('position')
        model = data.get('model')

        minn = 10
        cnt = Charge.query.count()
        minn = minn + int(cnt/3)

        cha = Charge(name=name,parking=parking,position=position,model=model,create_date=datetime.now(),expected_time=minn)


        db.session.add(cha)
        db.session.commit()
        print(f"성공 Received name: {name}, parking: {parking}, position: {position}, model: {model}")
        return redirect(url_for('main.index'))

    return render_template('pages/charging.html')

@bp.route('/mypage')
@login_required
def my_page():
    car_list = Charge.query.filter_by(name=g.user.name).order_by(Charge.create_date.desc())
    return render_template('pages/mypage.html',car_list=car_list)

@bp.route('/submit', methods=['POST','GET'])
def submit():
    data = request.get_json()
    name = data.get('name')
    parking = data.get('parking')
    position = data.get('position')
    model = data.get('model')
    print(f"Received name: {name}, parking: {parking}, position: {position}, model: {model}")
    return jsonify({'name':name,'parking':parking,'position':position,'model':model })

@bp.route('/queue')
def queue():
    return render_template('pages/selectList.html')

@bp.route('/samsung')
def samsung():
    car_list = Charge.query.filter_by(parking="삼성창조캠퍼스").order_by(Charge.create_date.asc())
    # car_list = Charge.query.filter_by(parking="대구테크비즈센터").order_by(Charge.create_date.asc())
    # car_list = Charge.query.order_by(Charge.create_date.asc())
    return render_template('pages/samsung.html', car_list=car_list)

@bp.route('/tech')
def tech():
    # car_list = Charge.query.filter_by(parking="삼성창조캠퍼스").order_by(Charge.create_date.asc())
    car_list = Charge.query.filter_by(parking="대구테크비즈센터").order_by(Charge.create_date.asc())
    # car_list = Charge.query.order_by(Charge.create_date.asc())
    return render_template('pages/tech.html', car_list=car_list)