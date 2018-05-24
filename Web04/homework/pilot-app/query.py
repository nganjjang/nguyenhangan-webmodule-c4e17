from models.service import Service
from models.customer import Customer
from models.user import User
import mlab

mlab.connect()

# all_service = Service.objects(gender=1) #objects la mot function() --> rat la tat ca objects of class service; all_service la dang list
# #lay ra tat ca objects gender = nam, co the query gia tri >, <, not just equal
# # first_service = all_service[0] #first_service la dang dictionary
#
# for index, service in enumerate(all_service): #enumerate de lay ca index va tung value cua tung phan tu cua list
#     print(service['name'])
#     if index == 9:
#         break
#
# # print(first_service['name']) #field la phan tu be nhat belongs to Document

# id_to_find = "5af59cdbfd860d2aebaa4c85"

# hera = Service.objects(id = id_to_find) #tra ve dang list 1 phan tu, ko nen dung cach nay
# # hera = Service.objects.get(id = id_to_find) #nen dung cach 2 & 3
# hera = Service.objects.with_id(id_to_find) #neu ko co id, se tra ket qua None
# if hera is not None:
#     # hera.delete()
#     # print("Deleted")
#     print(hera.address)
#     hera.update(set__address="Pham Van Dong",
#                 set__height=173)
#     hera.reload() #phai load lai variable hera da dc update tren mlab
#     print(hera.address)
# else:
#     print("Service not found")

# print(hera.to_mongo()) #do o dang dictionary nen co the print value of key theo cach nay, mongoengine cho phep dung .name
# print(hera['name'])

users = User.objects()
print(users[0]['email'])
