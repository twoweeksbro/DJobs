from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'info.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b',\xbc\xf1\xa8\x07\x1c\x1b\x81\x99\x1bj5?\xce\xb6\xde'
