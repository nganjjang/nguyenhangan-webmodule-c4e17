from models.service import Service
from faker import Faker
from random import randint, choice
import mlab

mlab.connect()

fake = Faker()

# print(fake.address())

for i in range(50):
    print('Saving service', i + 1, '.....')
    service = Service(name=fake.name(),
                        yob=randint(1990, 2000),
                        gender=randint(0, 1),
                        height=randint(150, 190),
                        phone=fake.phone_number(),
                        address=fake.address(),
                        status=choice([True, False])) #lay 1 form cua class Service de dien form

    service.save() #save vao tu
