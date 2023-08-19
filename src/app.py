from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Load the config file
app.config.from_object('config')

# region configure the SQLite database, relative to the app instance folder
db = SQLAlchemy()  # create the extension
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
db.init_app(app)  # initialize the app with the extension
# endregion

# region Import models
from src.models.author import Author
from src.models.editorial import Editorial
from src.models.book import Book
# endregion

# region Import views
from src.views import register_api, MetaApiView
# serializers
from src.serializers.author import AuthorSerializer
from src.serializers.editorial import EditorialSerializer
from src.serializers.book import BookSerializer
# forms
from src.forms.author import AuthorForm
from src.forms.editorial import EditorialForm
from src.forms.book import BookForm

# create routes
register_api(app, name='authors', meta=MetaApiView(Author, AuthorSerializer, form=AuthorForm))
register_api(app, name='editorials', meta=MetaApiView(Editorial, EditorialSerializer, form=EditorialForm))
register_api(app, name='books', meta=MetaApiView(Book, BookSerializer, form=BookForm))
# endregion
