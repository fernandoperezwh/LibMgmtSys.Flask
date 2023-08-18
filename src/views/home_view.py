# flask imports
from flask import render_template
# local imports
from src.app import app


@app.route("/")
def home():
    return render_template('index.html')
