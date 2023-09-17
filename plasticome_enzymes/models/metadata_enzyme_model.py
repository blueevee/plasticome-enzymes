from peewee import Model, TextField

from .config import database


class BaseModel(Model):
    class Meta:
        database = database


class EnzymeMetadata(BaseModel):
    article_doi = TextField()
    enzyme_name = TextField()
    cazy_family = TextField()
    ec_number = TextField()
    genbank_accession = TextField()
    refseq_accession = TextField()

class PlasticTypes(BaseModel):
    plastic_name = TextField()
    acronym = TextField()


# database.connect()
# database.create_tables([FungiEnzyme])
# database.close()
