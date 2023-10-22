from plasticome_metadata.services.plastic_service import (
    store_plastic,
    search_plastic_by_acronym,
    search_plastics,
    update_plastic_by_id,
    delete_plastic_by_id,
)


def save_plastic(data: dict):
    """
    The function `save_plastic` saves plastic data if all required fields are
    provided, otherwise it returns an error message indicating the missing fields.

    :param data: The `data` parameter is a dictionary that contains information
    about a plastic. It should have the following keys:
    :type data: dict
    :return: a dictionary with either the result or an error message, along with an
    HTTP status code. If all the required fields are present in the data
    dictionary, the function calls the `store_plastic` function and returns the
    result along with a status code of 201 (created). If there is an error during
    the `store_plastic` function call, the function returns an error message along
    """
    try:
        required_fields = ['plastic_name', 'acronym']
        if all(data.get(field) for field in required_fields):
            result, error = store_plastic(**data)
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


def get_plastic(acronym: str):
    try:
        if acronym:
            result, error = search_plastic_by_acronym(acronym)
            if error:
                return {'error': 'plastic not found'}, 404
            return result, 200
        else:
            return {
                'error': 'Incomplete model, you must have to send a valid Acronym: `acronym`'
            }, 422
    except Exception as e:
        return {'error': f'Invalid data: {e}'}, 400


def get_all_plastics():
    """
    The function `get_all_plastics` retrieves a list of plastic objects and returns
    them as a JSON response, or returns an error message if there is an issue.

    :return: a list of dictionaries containing the id, plastic_name, and
    acronym of each plastic. If there is an error, it returns a dictionary
    with the error message and a corresponding HTTP status code.
    """
    try:
        result, error = search_plastics()
        if error:
            return {'error': str(error)}, 500

        plastic_list = [
            {
                'id': plastic.id,
                'plastic_name': plastic.plastic_name,
                'acronym': plastic.acronym,
            }
            for plastic in result
        ]

        return plastic_list, 200
    except Exception as e:
        return {'error': f'Invalid data: {e}'}, 400


def update_plastic(plastic_id: int, data: dict):
    """
    The function `update_plastic` updates a plastic record in a database based on
    the provided plastic ID and data.

    :param plastic_id: The plastic_id parameter is an integer that represents the
    ID of the plastic record that needs to be updated
    :type plastic_id: int
    :param data: The `data` parameter is a dictionary that contains the updated
    information for a plastic record. The keys in the dictionary represent the
    fields of the plastic record, and the values represent the updated values for
    those fields
    :type data: dict
    :return: The function `update_plastic` returns a dictionary with the following
    keys:
    """
    try:
        fields = ['plastic_name', 'plastic_acronym']
        formated_data = {
            key: value
            for key, value in data.items()
            if value is not None and value != '' and key in fields
        }
        result, error = update_plastic_by_id(plastic_id, formated_data)
        if error:
            return {'error': str(error)}, 500
        if result:
            return {'message': f'{result} record updated'}, 200
        return {'message': f'No records found'}, 404
    except Exception as e:
        return {'error': f'Invalid data: {e}'}, 400


def delete_plastic(plastic_id: int):
    """
    The function `delete_plastic` deletes a plastic record by its ID and returns a
    success message or an error message.

    :param plastic_id: The `plastic_id` parameter is an integer that represents the
    unique identifier of the plastic record that needs to be deleted
    :type plastic_id: int
    :return: a dictionary with either an 'error' key and value or a 'message' key
    and value, along with an HTTP status code.
    """
    try:
        _, error = delete_plastic_by_id(plastic_id)
        if error:
            return {'error': str(error)}, 500
        return {'message': f'Record deleted'}, 200
    except Exception as e:
        return {'error': f'Invalid data: {e}'}, 400
