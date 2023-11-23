from plasticome_metadata.models.metadata_enzyme_model import EnzymeMetadata


def store_enzyme(
    enzyme_name: str,
    article_doi: str = None,
    cazy_family: str = None,
    ec_number: str = None,
    protein_sequence: str = None,
    genbank_protein_id: str = None,
    fungi_name: str = None,
) -> (dict, None):

    """
    The function `store_enzyme` stores enzyme metadata in a database and returns
    the saved enzyme data or an error if the operation fails.

    :param enzyme_name: The name of the enzyme
    :param fungi_name: The `fungi_name` parameter is a string that represents the
    name of the fungi associated with the enzyme
    :param article_doi: The article DOI is a unique identifier for a scientific
    article. It stands for "Digital Object Identifier" and is used to provide a
    persistent link to the article online
    :param cazy_family: The `cazy_family` parameter represents the CAZy
    (Carbohydrate-Active enZYmes) family to which the enzyme belongs. CAZy is a
    database that classifies enzymes involved in the synthesis, modification, and
    degradation of carbohydrates
    :param ec_number: The `ec_number` parameter is a string that represents the
    Enzyme Commission (EC) number of the enzyme. The EC number is a numerical
    classification system for enzymes based on the reactions they catalyze. It
    consists of four numbers separated by periods, such as "1.1.1
    :param protein_sequence: The parameter `protein_sequence` is a string that
    represents the amino acid sequence of the enzyme protein
    :param genbank_protein_id: The `genbank_protein_id` parameter is a string
    that represents the GenBank assembly ID of the organism from which the enzyme
    was obtained. GenBank is a database that provides annotated DNA sequences for
    various organisms. The assembly ID refers to a specific version of the genome
    assembly for a particular organism
    :return: The function `store_enzyme` returns a tuple containing two elements.
    The first element is a dictionary representing the data of the saved enzyme,
    and the second element is either `None` if the enzyme was successfully saved or
    an error object if an exception occurred during the saving process.
    """

    try:

        saved_enzyme = EnzymeMetadata.create(
            enzyme_name=enzyme_name,
            ec_number=ec_number,
            article_doi=article_doi,
            cazy_family=cazy_family,
            fungi_name=fungi_name,
            protein_sequence=protein_sequence,
            genbank_protein_id=genbank_protein_id,
        )

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
        enzymes = (
            EnzymeMetadata.select()
            .where(EnzymeMetadata.ec_number == ec_number)
        )
        enzyme_list = [enzyme.__data__ for enzyme in enzymes]
        return enzyme_list, None
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
            EnzymeMetadata.select().where(EnzymeMetadata.id == enzyme_id).get()
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
        all_enzymes = EnzymeMetadata.select()
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
        query = EnzymeMetadata.update(**data).where(
            EnzymeMetadata.id == enzyme_id
        )
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

        enzyme_to_delete = EnzymeMetadata.get(EnzymeMetadata.id == enzyme_id)
        enzyme_to_delete.delete_instance()
        return True, None
    except Exception as error:
        return None, error
