from flask import Flask, request, jsonify
from flask_pydantic_spec import FlaskPydanticSpec
from plasticome_enzymes.controllers.enzyme_controller import (
    get_enzyme,
    save_enzyme_controller,
)

server = Flask(__name__)
spec = FlaskPydanticSpec(
    'flask', title='PLASTICOME ENZYMES DEMO', version='v1.0', path='docs'
)
spec.register(server)


@server.get('/find/<ec_number>')
def get_plasticome_route(ec_number):
    return get_enzyme(ec_number)


@server.post('/save')
def save_enzyme_route():
    return save_enzyme_controller(request.json)


server.run()
