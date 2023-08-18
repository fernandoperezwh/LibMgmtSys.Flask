from src.app import app


@app.route('/authors/list')
def list_authors():
    return "<p>List authors</p>"


@app.route('/authors/create')
def create_authors():
    return "<p>Create authors</p>"


@app.route('/authors/<author_id>/detail')
def detail_authors():
    return "<p>Detail author</p>"


@app.route('/authors/<author_id>/update')
def update_authors():
    return "<p>Update author</p>"


@app.route('/authors/<author_id>/delete')
def delete_authors():
    return "<p>Delete author</p>"
