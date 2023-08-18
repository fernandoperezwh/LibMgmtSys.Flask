from src.app import app


@app.route('/books/list')
def list_books():
    return "<p>List books</p>"


@app.route('/books/create')
def create_books():
    return "<p>Create books</p>"


@app.route('/books/<book_id>/detail')
def detail_books():
    return "<p>Detail book</p>"


@app.route('/books/<book_id>/update')
def update_books():
    return "<p>Update book</p>"


@app.route('/books/<book_id>/delete')
def delete_books():
    return "<p>Delete book</p>"
