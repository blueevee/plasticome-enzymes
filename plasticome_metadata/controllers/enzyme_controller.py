from plasticome_metadata.services.enzyme_service import (
    delete_enzyme_by_id,
    search_enzyme,
    search_enzyme_by_ec_number,
    search_enzyme_by_id,
    store_enzyme,
    update_enzyme_by_id,
)


def get_enzyme(enzyme_id: str):
    try:
        if enzyme_id:
            result, error = search_enzyme_by_id(enzyme_id)
            if error:
                return {'error': 'enzyme not found'}, 404
            return result, 200
        else:
            return {
                'error': 'Incomplete model, you must have to send a valid: `enzyme_id`'
            }, 422
    except Exception as e:
        return {'error': f'Invalid data: {e}'}, 400


def get_enzyme_by_ec(ec_number: str):
    try:
        if ec_number:
            result, error = search_enzyme_by_ec_number(ec_number)
            if error:
                return {'error': 'enzyme not found'}, 404
            return result, 200
        else:
            return {
                'error': 'Incomplete model, you must have to send a valid: `ec_number`'
            }, 422
    except Exception as e:
        return {'error': f'Invalid data: {e}'}, 400


def get_all_enzyme():
    try:
        result, error = search_enzyme()
        if error:
            return {'error': str(error)}, 500

        enzyme_list = [
            {
                'id': enzyme.id,
                'enzyme_name': enzyme.enzyme_name,
                'ec_number': enzyme.ec_number,
                'article_doi': enzyme.article_doi,
                'fungi_name': enzyme.fungi_name,
                'cazy_family': enzyme.cazy_family,
                'protein_sequence': enzyme.protein_sequence,
                'genbank_protein_id': enzyme.genbank_protein_id,
            }
            for enzyme in result
        ]

        return enzyme_list, 200
    except Exception as e:
        return {'error': f'Invalid data: {e}'}, 400


def save_enzyme(data: dict):
    try:
        result, error = store_enzyme(**data)
        if error:
            return {'error': str(error)}, 500
        return result, 201
    except Exception as e:
        return {'error': f'Invalid data: {e}'}, 400


def update_enzyme(enzyme_id: int, data: dict):
    try:
        fields = [
            'article_doi',
            'enzyme_name',
            'cazy_family',
            'ec_number',
            'protein_sequence',
            'genbank_protein_id',
            'fungi_name',
        ]
        formated_data = {
            key: value
            for key, value in data.items()
            if value is not None and value != '' and key in fields
        }
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
