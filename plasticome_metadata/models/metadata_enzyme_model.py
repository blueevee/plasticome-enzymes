from peewee import Model, CharField, TextField, ForeignKeyField

from plasticome_metadata.models.config import database


class BaseModel(Model):
    class Meta:
        database = database

class PlasticTypes(BaseModel):
    plastic_name = CharField()
    acronym = CharField()

class EnzymeMetadata(BaseModel):
    cazy_family = CharField(null=True)
    fungi_name = CharField(null=True)
    enzyme_name = CharField()
    ec_number = CharField(null=True)
    protein_sequence = TextField(null=True)
    article_doi = CharField(null=True)
    genbank_assembly_id = CharField(null=True)
    plastic_type = ForeignKeyField(PlasticTypes, backref='associated_enzymes')


# database.connect()
# database.create_tables([PlasticTypes, EnzymeMetadata])
# database.close()
