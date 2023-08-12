from plasticome_enzymes.services.enzyme_service import (
    search_enzyme,
    store_enzyme,
    search_enzyme_by_ec_number,
    update_enzyme_by_id,
    delete_enzyme_by_id,
)


def get_enzyme(ec_number: str):
    try:
        if ec_number:
            result, error = search_enzyme_by_ec_number(ec_number)
            if error:
                # TRATAR QANDO N EXISTE
                return {'error': str(error)}, 500
            return result, 200
        else:
            return {
                'error': 'Incomplete model, you must have to send a valid EC number: `ec_number`'
            }, 422
    except Exception as e:
        return {'error': f'Invalid data: {e}'}, 400

def get_all_enzyme():
    try:
        result, error = search_enzyme()
        if error:
            return {'error': str(error)}, 500
        enzyme_list = list(map(lambda enzyme: {'id': enzyme.id, 'enzyme': enzyme.enzyme, 'ec_number': enzyme.ec_number}, result))
        return enzyme_list, 200
    except Exception as e:
        return {'error': f'Invalid data: {e}'}, 400


def save_enzyme(data: dict):
    try:
        if data.get('enzyme', False) and data.get('ec_number', False):
            result, error = store_enzyme(**data)
            if error:
                return {'error': str(error)}, 500
            return result, 201
        else:
            return {
                'error': 'Incomplete model, you must have to send a valid enzyme name: `enzyme` and a valid EC number: `ec_number`'
            }, 422
    except Exception as e:
        return {'error': f'Invalid data: {e}'}, 400


def update_enzyme(enzyme_id: int, data: dict):
    try:
        formated_data = {key: value for key, value in data.items() if value is not None and value != '' and key in ['enzyme', 'ec_number']}
        result, error = update_enzyme_by_id(enzyme_id, formated_data)
        if error:
            return {'error': str(error)}, 500
        if result:
            return {'message': f'{result} record updated'}, 200
        return {'message': f'No records found'}, 404
    except Exception as e:
        return {'error': f'Invalid data: {e}'}, 400


def delete_enzyme(enzyme_id: int):
    try:
        result, error = delete_enzyme_by_id(enzyme_id)
        if error:
            return {'error': str(error)}, 500
        if result:
            return {'message': f'Record deleted'}, 200
    except Exception as e:
        return {'error': f'Invalid data: {e}'}, 400
