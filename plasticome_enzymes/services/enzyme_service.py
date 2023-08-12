from plasticome_enzymes.models.enzyme_model import FungiEnzyme


def store_enzyme(enzyme: str, ec_number: str) -> (dict,None):
    """
    Save an enzyme in the database.

    Parameters:
        enzyme (str): The name of the enzyme to be saved.
        ec_number (str): The associated EC number of the enzyme.

    Returns:
        enzyme (dict): The new enzyme created.
    """
    try:
        saved_enzyme = FungiEnzyme.create(enzyme=enzyme, ec_number=ec_number)
        return saved_enzyme.__data__, None
    except Exception as error:
        return None, error


def search_enzyme_by_ec_number(ec_number: str):
    """
    Search an enzyme in the database.

    Parameters:
        ec_number (str): The EC number of the enzyme.

    Returns:
        enzyme (dict): The registered enzyme.
    """
    try:
        enzyme = (
            FungiEnzyme.select()
            .where(FungiEnzyme.ec_number == ec_number)
            .get()
        )
        return enzyme.__data__, None
    except Exception as error:
        return None, error


def search_enzyme_by_id(enzyme_id: str):
    """
    Search an enzyme in the database.

    Parameters:
        id (str): The identifier of the enzyme.

    Returns:
        enzyme (dict): The registered enzyme.
    """
    try:
        enzyme = (
            FungiEnzyme.select()
            .where(FungiEnzyme.id == enzyme_id)
            .get()
        )
        return enzyme.__data__, None
    except Exception as error:
        return None, error


def search_enzyme():
    """
    Search all enzymes in the database.

    Returns:
        enzymes (dict): All the records.
    """
    try:
        all_enzymes = FungiEnzyme.select()
        return all_enzymes, None
    except Exception as error:
        return None, error


def update_enzyme_by_id(enzyme_id: int, data: dict):
    """
    Update an enzyme in the database.

    Parameters:
        id (int): The identifier of enzyme's register.
        data (dict): Fields to update.

    Returns:
        result: Number of altered registers
    """
    try:
        query = FungiEnzyme.update(**data).where(FungiEnzyme.id == enzyme_id)
        result = query.execute()
        return result, None
    except Exception as error:
        return None, error


def delete_enzyme_by_id(enzyme_id: str):
    """
    Search an enzyme in the database.

    Parameters:
        id (str): The identifier of the enzyme.

    Returns:
        enzyme (dict): The registered enzyme.
    """
    try:

        enzyme_to_delete = FungiEnzyme.get(FungiEnzyme.id == enzyme_id)
        enzyme_to_delete.delete_instance()
        return True, None
    except Exception as error:
        return None, error