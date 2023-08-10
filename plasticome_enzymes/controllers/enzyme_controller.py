from plasticome_enzymes.services.enzyme_service import (
    save_enzyme,
    search_enzyme_by_ec_number,
)


def get_enzyme(ec_number: str):
    try:
        if ec_number:
            result, error = search_enzyme_by_ec_number(ec_number)
            if error:
                return {'error': str(error)}, 500
            return result, 200
        else:
            return {
                'error': 'Incomplete model, you must have to send a valid EC number: `ec_number`'
            }, 422
    except Exception as e:
        return {'error': f'Invalid data: {e}'}, 400


def save_enzyme_controller(data: dict):
    try:
        if data.get('enzyme', False) and data.get('ec_number', False):
            result, error = save_enzyme(**data)
            if error:
                return {'error': str(error)}, 500
            return result, 201
        else:
            return {
                'error': 'Incomplete model, you must have to send a valid enzyme name: `enzyme` and a valid EC number: `ec_number`'
            }, 422
    except Exception as e:
        return {'error': f'Invalid data: {e}'}, 400
