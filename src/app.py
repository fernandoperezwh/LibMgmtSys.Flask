from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()

app = Flask(
    __name__,
)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
db.init_app(app)  # initialize the app with the extension

# Import views
from src.views import *

# Import models
from src.models.author import Author
from src.models.editorial import Editorial
from src.models.book import Book

# Load the config file
app.config.from_object('config')
