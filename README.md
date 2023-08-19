# Library Management System - Flask


## Installation

Create a virtual environment using pipenv.
```bash
pipenv shell
```

Download and install dependencies with the next commmand.
```bash
pipenv install
```

Open the flask app shell with `flask --app manage shell` and run the next script to 
create the project database with the models.
```python
from src.app import app, db

with app.app_context():
    db.create_all()
```

[Optional] Load dummy data to the database
```bash
sqlite3 instance/db.sqlite3 < src/.config/fixtures/dump_authors.sql
sqlite3 instance/db.sqlite3 < src/.config/fixtures/dump_editorial.sql
sqlite3 instance/db.sqlite3 < src/.config/fixtures/dump_book.sql
```

## Usage

Start development server with the next command.
```bash
flask --app manage run
```
