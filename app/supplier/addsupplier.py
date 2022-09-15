import json
from app.models import Supplier
from app import db
import uuid
from flask import request, jsonify


def addNewSupplier():
    '''create a new supplier item'''
    data = request.get_json()

    if data and data is not None:
        name=data['name']
        location=data['location']
        momo_number=data['momo_number']
        description=data['description']
       


        supplier=Supplier(
            name=name,
            location=location,
            momo_number=momo_number,
            description=description

        )
        db.session.add(supplier)
        db.session.commit()


        return json.dumps({
            'id':supplier.id,'name':supplier.name,'location':supplier.location,'momo_number':supplier.momo_number,'description':supplier.description
        },sort_keys=True, indent=4, default=str
        )
        

        