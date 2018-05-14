from models.service import Service
from models.customer import Customer
import mlab

mlab.connect()

all_service = Service.objects(gender=1) #objects la mot function() --> rat la tat ca objects of class service; all_service la dang list
#lay ra tat ca objects gender = nam, co the query gia tri >, <, not just equal
# first_service = all_service[0] #first_service la dang dictionary

for index, service in enumerate(all_service): #enumerate de lay ca index va tung value cua tung phan tu cua list
    print(service['name'])
    if index == 9:
        break

# print(first_service['name']) #field la phan tu be nhat belongs to Document
