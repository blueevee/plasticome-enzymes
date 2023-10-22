from plasticome_metadata.services.user_service import verify_credentials


def authenticate_user(data: dict):
    try:
        required_fields = ['username', 'secret']
        if all(data.get(field) for field in required_fields):
            result, error = verify_credentials(
                data['username'], data['secret']
            )
            if error:
                return {'error': str(error)}, 401
            return {'access_token': result}, 200
        else:
            missing_fields = [
                field for field in required_fields if not data.get(field)
            ]
            return {
                'error': f'Incomplete model, missing fields: {", ".join(missing_fields)}'
            }, 422
    except Exception as error:
        return {'[AUTH USER]': error}, 400
