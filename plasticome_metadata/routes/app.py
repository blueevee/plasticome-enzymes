from flask import Flask, request
from flask_pydantic_spec import FlaskPydanticSpec

from plasticome_metadata.controllers.enzyme_controller import (
    delete_enzyme,
    get_all_enzyme,
    get_enzyme,
    save_enzyme,
    update_enzyme,
)

server = Flask(__name__)
spec = FlaskPydanticSpec(
    'flask', title='PLASTICOME ENZYMES DEMO', version='v1.0', path='docs'
)
spec.register(server)


@server.get('/enzyme_find')
def get_all_enzyme_route():
    return get_all_enzyme()


@server.get('/enzyme_find/<ec_number>')
def get_enzyme_route(ec_number):
    return get_enzyme(ec_number)


@server.post('/enzyme_save')
def save_enzyme_route():
    return save_enzyme(request.json)


@server.patch('/enzyme_update/<int:id>')
def update_enzyme_route(id):
    data = request.json
    return update_enzyme(id, data)


@server.delete('/enzyme_delete/<int:id>')
def delete_enzyme_route(id):
    return delete_enzyme(id)


server.run()
