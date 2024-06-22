from hello import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id',ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    log_id = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    car = db.Column(db.String(200))
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True, nullable=False)

class Charge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    parking = db.Column(db.String(50))
    position = db.Column(db.String(20))
    model = db.Column(db.String(100))
    create_date = db.Column(db.DateTime())
    expected_time = db.Column(db.String(100))