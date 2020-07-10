import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ["flaskKey"]
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["evalDB"]
db = SQLAlchemy(app)

from prodmgreval import routes
