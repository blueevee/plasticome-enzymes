from plasticome_enzymes.models.metadata_enzyme_model import EnzymeMetadata


def store_enzyme(
    enzyme_name: str,
    ec_number: str,
    article_doi: str,
    cazy_family: str,
    genbank_accession: str,
    refseq_accession: str,
) -> (dict, None):
    """
    Save an enzyme in the database.

    Parameters:
        enzyme (str): The name of the enzyme to be saved.
        ec_number (str): The associated EC number of the enzyme.
        article_doi (str): DOI of the article where the enzyme was found.
        cazy_family (str): Family cazy of the enzyme.
        genbank_accession (str): Genbank accession number.
        refseq_accession (str): RefSeq accession number.

    Returns:
        enzyme (dict): The new enzyme created.
    """
    try:
        saved_enzyme = EnzymeMetadata.create(
            enzyme_name=enzyme_name,
            ec_number=ec_number,
            article_doi=article_doi,
            cazy_family=cazy_family,
            genbank_accession=genbank_accession,
            refseq_accession=refseq_accession,
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
        enzyme = (
            EnzymeMetadata.select()
            .where(EnzymeMetadata.ec_number == ec_number)
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
