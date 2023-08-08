from peewee import Model, TextField
from .config import database


class BaseModel(Model):
    class Meta:
        database = database


class FungiEnzyme(BaseModel):
    enzyme = TextField()
    ec_number = TextField()



# database.connect()
# database.create_tables([FungiEnzyme])
# database.close()





