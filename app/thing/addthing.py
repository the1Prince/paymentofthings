import json
from app.models import Thing
from app import db
import uuid
from flask import request, jsonify


def addNewThing():
    '''create a new thing object'''
    data = request.get_json()

    if data and data is not None:
        unique_name=data['unique_name']
        shelf_life=data['shelf_life']
        electric_consumption=data['electric_consumption']
        description=data['description']
        device_id=data['device_id']
        brand_id=data['brand_id']
        


        thing=Thing(
            unique_name=unique_name,
            shelf_life=shelf_life,
            electric_consumption=electric_consumption,
            description=description,
            device_id=device_id,
            brand_id=brand_id

        )
        db.session.add(thing)
        db.session.commit()


        return json.dumps({
            'id':thing.id,'unique_name':thing.unique_name,'shelf_life':thing.shelf_life,'electric_consumption':thing.electric_consumption,'description':thing.description,'device_id':thing.device_id,'brand_id':thing.brand_id
        },sort_keys=True, indent=4, default=str
        )
        

        