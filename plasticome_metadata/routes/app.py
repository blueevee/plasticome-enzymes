from flask import Flask, request
from flask_pydantic_spec import FlaskPydanticSpec

from plasticome_metadata.controllers.enzyme_controller import (
    delete_enzyme,
    get_all_enzyme,
    get_enzyme,
    save_enzyme,
    update_enzyme,
)
from plasticome_metadata.controllers.plastic_controller import (
    save_plastic,
    update_plastic,
    delete_plastic,
    get_all_plastics,
    get_plastic,
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


@server.get('/plastic_find')
def get_all_plastics_route():
    return get_all_plastics()


@server.get('/plastic_find/<acronym>')
def get_plastic_route(acronym):
    return get_plastic(acronym)


@server.post('/plastic_save')
def save_plastic_route():
    return save_plastic(request.json)


@server.patch('/plastic_update/<int:id>')
def update_plastic_route(id):
    data = request.json
    return update_plastic(id, data)


@server.delete('/plastic_delete/<int:id>')
def delete_plastic_route(id):
    return delete_plastic(id)


server.run()
