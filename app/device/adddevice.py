from email.mime import image
import json
from app.models import Device
from app import db
import uuid
from flask import request, jsonify


def addNewDevice():
    '''create a new device item'''
    data = request.get_json()

    if data and data is not None:
        name=data['name']
        description=data['description']
        image=data['image']
        category_id=data['category_id']


        device=Device(
            name=name,
            description=description,
            image=image,
            category_id=category_id

        )
        db.session.add(device)
        db.session.commit()


        return json.dumps({
            'id':device.id,'name':device.name,'description':device.description,'image':device.image,'category_id':device.category_id
        },sort_keys=True, indent=4, default=str
        )
        

        