from mongoengine import *
import mlab
from models.service import Service

mlab.connect()

#Exercise 2:
id_to_find = "5af5a25ffd860d362f53a263"

# Cach 1:
document_to_find = Service.objects(id = id_to_find)
for index, service in enumerate(document_to_find):
    print(service['name'])

#Cach 2:
document_to_find = Service.objects.get(id = id_to_find)
print(document_to_find['name'])

#Exercise 3:
id_to_delete = "5af59af1fd860d272ead4611" #dung _id khac de ko anh huong den ex2
document_to_del = Service.objects.get(id = id_to_delete)
document_to_del.delete()
