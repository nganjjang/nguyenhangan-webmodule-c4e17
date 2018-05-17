from flask import * #Flask, render_template, redirect, url_for
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

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html', all_service=all_service)

@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects.with_id(service_id)
    if service_to_delete is not None:
        service_to_delete.delete()
        return redirect(url_for('admin'))
    else:
        return "Service not found"



@app.route('/new-service', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('new-service.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        gender = form['gender']
        new_service = Service(name=name, yob=yob, phone=phone, gender=gender)
        new_service.save()
        return redirect(url_for('admin'))

@app.route('/service')
def service():
    all_service = Service.objects()
    return render_template('service.html', all_service=all_service)

@app.route('/detail/<service_id>')
def detail(service_id):
    service_detail = Service.objects.with_id(service_id)
    print(service_id)
    return render_template('detail.html', service_detail=service_detail)

@app.route('/update-service/<service_id>', methods=['GET', 'POST'])
def update(service_id):
    if request.method == 'GET':
        service_to_update = Service.objects.with_id(service_id)
        return render_template ('update-service.html', service_to_update=service_to_update)
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        gender = form['gender']
        height = form['height']
        phone = form['phone']
        address = form['address']
        # status = form['status']
        description = form['description']
        measurements = form['measurements']
        image = form['image']
        service_to_update = Service.objects.with_id(service_id)
        service_to_update.update(set__name=name,
                                    set__yob=yob,
                                    set__gender=gender,
                                    set__height=height,
                                    set__phone=phone,
                                    set__address=address,
                                    # set__status=status,
                                    set__description=description,
                                    set__measurements=measurements,
                                    set__image=image)
        service_to_update.reload()
        return redirect(url_for('admin'))


if __name__ == '__main__':
  app.run(debug=True)
