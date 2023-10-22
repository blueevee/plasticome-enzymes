from plasticome_metadata.services.enzyme_plastic_service import (
    add_plastic_type_to_enzyme,
    get_plastic_types_for_enzyme,
    get_all_plastic_types_enzyme,
    remove_plastic_type_from_enzyme,
)


def save_plastic_enzyme(data: dict):
    try:
        required_fields = ['enzyme', 'plastic_type']
        if all(data.get(field) for field in required_fields):
            result, error = add_plastic_type_to_enzyme(**data)
            if error:
                return {'error': str(error)}, 500
            return result, 201
        else:
            missing_fields = [
                field for field in required_fields if not data.get(field)
            ]
            return {
                'error': f'Incomplete model, missing fields: {", ".join(missing_fields)}'
            }, 422
    except Exception as e:
        return {'error': f'Invalid data: {e}'}, 400


def get_plastic_enzymes(enzyme_id: str):
    try:
        if enzyme_id:
            result, error = get_plastic_types_for_enzyme(enzyme_id)
            if error:
                return {'error': 'not found plastics for this enzyme'}, 404
            return result, 200
        else:
            return {
                'error': 'Incomplete model, you must have to send a valid: `enzyme_id`'
            }, 422
    except Exception as e:
        return {'error': f'Invalid data: {e}'}, 400


def get_all_plastic_enzyme():
    try:
        result, error = get_all_plastic_types_enzyme()
        if error:
            return {'error': str(error)}, 500

        return result, 200
    except Exception as e:
        return {'error': f'Invalid data: {e}'}, 400


def delete_plastic_enzyme(registered_id: int):
    try:
        result, error = remove_plastic_type_from_enzyme(registered_id)
        if error:
            return {'error': str(error)}, 500
        if result:
            return {'message': f'Record deleted'}, 200
    except Exception as e:
        return {'error': f'Invalid data: {e}'}, 400
