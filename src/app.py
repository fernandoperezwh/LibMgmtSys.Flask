from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()

app = Flask(
    __name__,
)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"

# Add views
from src.views import *

# Load the config file
app.config.from_object('config')

