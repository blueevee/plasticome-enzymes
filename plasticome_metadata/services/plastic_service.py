from plasticome_metadata.models.metadata_enzyme_model import PlasticTypes


def store_plastic(plastic_name: str, plastic_acronym: str) -> (dict, None):
    """
    Save a plastic in the database.

    Parameters:
        plastic_name (str): name of the plastic to be saved.
        plastic_acronym (str): The associated acronym to the plastic.

    Returns:
        plastic (dict): The new plastic's register created.
    """
    try:
        registered_plastic = PlasticTypes.create(
            plastic_name=plastic_name, acronym=plastic_acronym
        )
        return registered_plastic.__data__, None
    except Exception as error:
        return None, error


def search_plastic_by_id(id: str):
    """
    Search a plastic in the database.

    Parameters:
        id (str): identifier of the plastic.

    Returns:
        plastic (dict): The registered plastic.
    """
    try:
        plastic = PlasticTypes.select().where(PlasticTypes.id == id).get()
        return plastic.__data__, None
    except Exception as error:
        return None, error


def search_plastic_by_acronym(acronym: str):
    """
    Search a plastic in the database.

    Parameters:
        id (str): identifier of the plastic.

    Returns:
        plastic (dict): The registered plastic.
    """
    try:
        plastic = (
            PlasticTypes.select().where(PlasticTypes.acronym == acronym).get()
        )
        return plastic.__data__, None
    except Exception as error:
        return None, error


def search_associated_enzymes_by_acronym(acronym: str):
    """
    The function searches for associated enzymes based on a given acronym and
    returns the sequences if found, otherwise it returns an error.

    :param acronym: The parameter "acronym" is a string that represents the acronym
    of a plastic type
    :return:  returns a tuple containing two values.
    The first value is `sequences`, which represents the associated enzyme sequences
    found for the given acronym. The second value is `None` if no error occurred
    during the execution of the function. If an error occurred, the second value
    will be the `error` object that describes the error.
    """
    try:
        plastic = (
            PlasticTypes.select().where(PlasticTypes.acronym == acronym).get()
        )
        sequences = plastic.sequences
        return sequences, None
    except Exception as error:
        return None, error


def search_plastics():
    """
    Search all plastics in the database.

    Returns:
        plastics (dict): All the records.
    """
    try:
        all_plastics = PlasticTypes.select()
        return all_plastics, None
    except Exception as error:
        return None, error


def update_plastic_by_id(plastic_id: int, data: dict):
    """
    Update a plastic in the database.

    Parameters:
        id (int): The identifier of plastic's register.
        data (dict): Fields to update.

    Returns:
        result: Number of altered registers
    """
    try:
        query = PlasticTypes.update(**data).where(
            PlasticTypes.id == plastic_id
        )
        result = query.execute()
        return result, None
    except Exception as error:
        return None, error


def delete_plastic_by_id(plastic_id: str):
    """
    Search a plastic in the database.

    Parameters:
        id (str): The identifier of the plastic.

    Returns:
        plastic (dict): The registered plastic.
    """
    try:

        plastic_to_delete = PlasticTypes.get(PlasticTypes.id == plastic_id)
        plastic_to_delete.delete_instance()
        return True, None
    except Exception as error:
        return None, error
