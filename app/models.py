from app import db



class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(64))
    description=db.Column(db.Text())
    image=db.Column(db.Text())


class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(64))
    description=db.Column(db.Text())
    logo=db.Column(db.Text())


class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(64))
    description=db.Column(db.Text())
    image=db.Column(db.Text())
    category_id=db.Column(db.Integer)


class Thing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    unique_name= db.Column(db.String(64),unique=True)
    shelf_life= db.Column(db.Integer)
    electric_consumption= db.Column(db.Float)
    description=db.Column(db.Text())
    device_id= db.Column(db.Integer)
    brand_id=db.Column(db.Integer)
    



class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(64))
    location= db.Column(db.Text())
    momo_number= db.Column(db.String(20))
    description=db.Column(db.Text())

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name= db.Column(db.String(64))
    cost= db.Column(db.Float())
    cost_transport_per_mile= db.Column(db.Float())
    service_charge= db.Column(db.Float())
    description=db.Column(db.Text())
    supplier_id=db.Column(db.Integer)


class Order_details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_id= db.Column(db.Integer)
    quantity= db.Column(db.Integer)
    total_cost= db.Column(db.Float())
    cur_status= db.Column(db.String(64))
    description=db.Column(db.Text())

class Utility_meter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(64))
    image= db.Column(db.Text())
    recharge_amount= db.Column(db.String(64))
    treshold_amount= db.Column(db.String(64))
    description=db.Column(db.Text())