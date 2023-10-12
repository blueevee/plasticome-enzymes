from peewee import Model, CharField, TextField, ForeignKeyField

from plasticome_metadata.models.config import database


class BaseModel(Model):
    class Meta:
        database = database

class PlasticTypes(BaseModel):
    plastic_name = CharField()
    acronym = CharField()

class EnzymeMetadata(BaseModel):
    cazy_family = CharField()
    fungi_name = CharField()
    ec_number = CharField()
    protein_sequence = TextField()
    doi = CharField()
    plastic_type = ForeignKeyField(PlasticTypes, backref='associated_enzymes')

#  NOME DO PLASTICO, CAZYME, FUNGO, EC NUMBER, PROTEIN SEQUENCE, DOI ARTIGO))


# database.connect()
# database.create_tables([PlasticTypes, EnzymeMetadata])
# database.close()
