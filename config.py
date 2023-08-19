import os
# Place config variables here. One per line.

# Enable Flask's debugging features. Should be False in production
DEBUG = True

SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', 'una_clave_secreta_generada_aleatoriamente')

# Define the database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'

# Disable csrf protection in all views
WTF_CSRF_ENABLED = False
