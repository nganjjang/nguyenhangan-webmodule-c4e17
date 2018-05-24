from models.service import Service
from faker import Faker
from random import randint, choice
import mlab

mlab.connect()

fake = Faker()

# print(fake.address())

# for i in range(2):
#     print('Saving service', i + 1, '.....')
service = Service(name="Minh Hang", #lay 1 form cua class Service de dien form
                        yob=1987,
                        gender=0,
                        height=165,
                        phone='0916596917',
                        address='Saigon',
                        status=False,
                        description="diu dang, hat hay, cute, de thuong",
                        measurements=[85, 65, 90],
                        image='https://images.vov.vn/w600/uploaded/usobwtngx2k/2017_08_08/145210-3.jpg')

service.save() #save vao tu
