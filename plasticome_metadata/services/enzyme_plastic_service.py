from plasticome_metadata.models.metadata_enzyme_model import EnzymePlasticTypes, PlasticTypes, EnzymeMetadata
from plasticome_metadata.services.plastic_service import search_plastic_by_acronym


def add_plastic_type_to_enzyme(enzyme: str, plastic_type: str):
    try:
        plastic_instance = search_plastic_by_acronym(plastic_type)[0]
        plastic_type = plastic_instance['id']

        saved_instance = EnzymePlasticTypes.create(enzyme_id=enzyme, plastic_id=plastic_type)

        return saved_instance.__data__, None
    except Exception as error:
        return None, error

def remove_plastic_type_from_enzyme(registered_id: int):
    try:
        query = EnzymePlasticTypes.delete().where(
            EnzymePlasticTypes.id == registered_id
        )
        query.execute()
        return True, None

    except Exception as error:
        return None, error

def get_plastic_types_for_enzyme(enzyme: str):
    try:

        query = (
            EnzymePlasticTypes
            .select(EnzymePlasticTypes, PlasticTypes.acronym)
            .join(PlasticTypes, on=(EnzymePlasticTypes.plastic_id == PlasticTypes.id))
            .where(EnzymePlasticTypes.enzyme_id == enzyme)
        )

        plastic_types = [{'plastic': result.plastic_id.acronym} for result in query]

        return plastic_types, None
    except Exception as error:
        print("ERROR", error)
        return None, error

def get_all_plastic_types_enzyme():
    try:
        all_enzymes = (EnzymePlasticTypes
                       .select(EnzymeMetadata.fungi_name, EnzymeMetadata.id.alias('enzyme_id'), EnzymeMetadata.enzyme_name, PlasticTypes.acronym.alias('plastic_acronym'))
                       .join(EnzymeMetadata, on=(EnzymePlasticTypes.enzyme_id == EnzymeMetadata.id))
                       .join(PlasticTypes, on=(EnzymePlasticTypes.plastic_id == PlasticTypes.id))
                       .dicts())
        return list(all_enzymes), None
    except Exception as error:
        return None, error
