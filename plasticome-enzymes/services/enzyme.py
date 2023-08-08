from models.enzyme import FungiEnzyme


def save_enzyme(enzyme: str, ec_number: str):
    """
    Save an enzyme in the database.

    Parameters:
        enzyme (str): The name of the enzyme to be saved.
        ec_number (str): The associated EC number of the enzyme.

    Returns:
        None
    """
    try:
        FungiEnzyme.create(enzyme=enzyme, ec_number=ec_number)
    except:
        ...

def search_enzyme(ec_number: str):
    """
    Search an enzyme in the database.

    Parameters:
        ec_number (str): The EC number of the enzyme.

    Returns:
        enzyme_name: The name of the enzyme searched
    """
    try:
        enzyme = FungiEnzyme.select().where(FungiEnzyme.ec_number == ec_number).get()
    except:
        ...