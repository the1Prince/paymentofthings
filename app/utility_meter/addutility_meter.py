import json
from app.models import Utility_meter
from app import db
import uuid
from flask import request, jsonify


def addNewUtilityMeter():
    '''create a new utiility meter'''
    data = request.get_json()

    if data and data is not None:
        name=data['name']
        image=data['image']
        recharge_amount=data['recharge_amount']
        treshold_amount=data['treshold_amount']
        description=data['description']
       


        utility=Utility_meter(
            name=name,
            image=image,
            recharge_amount=recharge_amount,
            treshold_amount=treshold_amount,
            description=description

        )
        db.session.add(utility)
        db.session.commit()


        return json.dumps({
            'id':utility.id,'name':utility.name,'image':utility.image,'recharge_amount':utility.recharge_amount,'treshold_amount':utility.treshold_amount,'description':utility.description
        },sort_keys=True, indent=4, default=str
        )
        

        