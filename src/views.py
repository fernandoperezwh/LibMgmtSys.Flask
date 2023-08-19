# flask imports
from flask import jsonify, request
from flask.views import MethodView
# local imports
from src.app import db


class MetaApiView:
    def __init__(self, model, serializer, **kwargs):
        self.model = model
        self.serializer = serializer
        self.form = kwargs.get('form', None)


class ListApiView(MethodView):
    """
    https://flask.palletsprojects.com/en/2.3.x/views/#method-dispatching-and-apis
    """
    init_every_request = False

    def __init__(self, meta):
        self.model = meta.model
        self.serializer = meta.serializer
        self.form = meta.form

    def get(self):
        items = self.model.query.all()
        serializer = self.serializer(many=True)
        return jsonify(serializer.dump(items))

    def post(self):
        # Validamos los datos que nos provee el usuario
        form = self.form()
        if not form.validate_on_submit():
            return jsonify(form.errors), 400
        # Creamos el registro de nuesto modelo
        instance = self.model()
        instance.from_json(**request.json)
        db.session.add(instance)
        db.session.commit()
        # Despues de guardar serializamos la instancia para devolver como respuesta
        serializer = self.serializer()
        return jsonify(serializer.dump(instance))


class DetailApiView(MethodView):
    init_every_request = False

    def __init__(self, meta):
        self.model = meta.model
        self.serializer = meta.serializer
        self.form = meta.form

    def _get_item(self, id):
        return self.model.query.get_or_404(id)

    def get(self, id):
        item = self._get_item(id)
        serializer = self.serializer()
        return jsonify(serializer.dump(item))

#     def patch(self, id):
#         item = self._get_item(id)
#         errors = self.validator.validate(item, request.json)
#
#         if errors:
#             return jsonify(errors), 400
#
#         item.update_from_json(request.json)
#         db.session.commit()
#         return jsonify(item.to_json())
#
    def delete(self, id):
        item = self._get_item(id)
        db.session.delete(item)
        db.session.commit()
        return jsonify({}), 204


def register_api(app, name, meta):
    app.add_url_rule(
        f"/{name}/",
        view_func=ListApiView.as_view(f"{name}-list", meta),
    )
    app.add_url_rule(
        f"/{name}/<int:id>/",
        view_func=DetailApiView.as_view(f"{name}-detail", meta)
    )
