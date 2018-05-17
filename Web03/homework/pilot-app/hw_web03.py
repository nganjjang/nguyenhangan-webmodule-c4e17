from mongoengine import *
import mlab
from models.service import Service

mlab.connect()

#Ex1: remove all documents in Service Collection
all_service_delete = Service.objects()
all_service_delete.delete()
