import json
from app.models import Stock
from app import db
import uuid
from flask import request, jsonify


def addNewStock():
    '''create a new stock item'''
    data = request.get_json()

    if data and data is not None:
        item_name=data['item_name']
        cost=data['cost']
        cost_transport_per_mile=data['cost_transport_per_mile']
        service_charge=data['service_charge']
        description=data['description']
        supplier_id=data['supplier_id']
       


        stock=Stock(
            item_name=item_name,
            cost=cost,
            cost_transport_per_mile=cost_transport_per_mile,
            service_charge=service_charge,
            description=description,
            supplier_id=supplier_id

        )
        db.session.add(stock)
        db.session.commit()


        return json.dumps({
            'id':stock.id,'item_name':stock.item_name,'cost':stock.cost,'cost_transport_per_mile':stock.cost_transport_per_mile,'service_charge':stock.service_charge,'description':stock.description,'supplier_id':stock.supplier_id
        },sort_keys=True, indent=4, default=str
        )
        

        