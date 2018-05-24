from mongoengine import * #import: StringField, IntField, BooleanField, Document

#design database:
#create collection (ten collection viet hoa letter dau tien)
class Service(Document): #inherit document tren mongodb
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
    description = StringField()
    measurements = ListField()
    image = StringField()
