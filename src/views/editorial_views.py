from src.app import app


@app.route('/editorials/list')
def list_editorials():
    return "<p>List editorials</p>"


@app.route('/editorials/create')
def create_editorials():
    return "<p>Create editorials</p>"


@app.route('/editorials/<editorial_id>/detail')
def detail_editorials():
    return "<p>Detail editorial</p>"


@app.route('/editorials/<editorial_id>/update')
def update_editorials():
    return "<p>Update editorial</p>"


@app.route('/editorials/<editorial_id>/delete')
def delete_editorials():
    return "<p>Delete editorial</p>"
