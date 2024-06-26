import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager


pymysql.install_as_MySQLdb()
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static/uploads')

app = Flask(__name__)
app.config.from_object('config')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
api = Api(app)
jwt = JWTManager(app)


from .models import produto_model, categoria_model, usuario_model
from .views import produto_views, categoria_view, usuario_views, login_viwes, refresh_toke_views