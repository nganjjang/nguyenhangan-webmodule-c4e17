from flask import Flask, render_template
from mongoengine import *
import mlab #from mlab import connect - another way
from models.service import Service
from models.customer import Customer

app = Flask(__name__)

mlab.connect()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<g>')
def search(g):
    all_service = Service.objects(gender=g, yob__lte = 2000, address__icontains = 'Hanoi') #doc them docs
    return render_template('search.html', all_service=all_service)


@app.route('/customer')
def customer():
    all_customer = Customer.objects()
    return render_template('customer.html', all_customer=all_customer)

@app.route('/customer/search')
def customer_search():
    all_customer = Customer.objects(gender=1, contacted=False)
    all_customer = all_customer[:10]
    return render_template('customer.html', all_customer=all_customer)

if __name__ == '__main__':
  app.run(debug=True)
