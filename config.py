from flask import Flask

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)



app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///storage.db"
app.config['SECRET_KEY'] = 'suco-de-uva'


db = SQLAlchemy(app)