import mlab
from mongoengine import *


mlab.connect()

class river(Document):
    name = StringField()
    continent = StringField()
    length = IntField()


all_river = river.objects(continent="S. America", length__lt=1000)
for river in all_river:
    print(river.to_mongo())
