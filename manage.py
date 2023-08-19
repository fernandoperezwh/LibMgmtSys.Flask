# python imports
import os
# local imports
from src.app import app

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run()