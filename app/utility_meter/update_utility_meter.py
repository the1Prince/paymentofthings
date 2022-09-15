from app import db
import json
from app.models import Utility_meter
from flask import request


def updateUtility():
    data=request.get_json()

    if data:
        id= data['id']
        name=data['name']
        image=data['image']
        recharge_amount=data['recharge_amount']
        treshold_amount=data['treshold_amount']
        description=data['description']

        utility=Utility_meter.query.filter_by(id=int(id)).first()

        if utility:
            utility.name=name
            utility.image=image
            utility.recharge_amount=recharge_amount
            utility.treshold_amount=treshold_amount
            utility.description=description

            db.session.commit()
            return json.dumps({
            'id':utility.id,'name':utility.name,'image':utility.image,'recharge_amount':utility.recharge_amount,'treshold_amount':utility.treshold_amount,'description':utility.description
            },sort_keys=True, indent=4, default=str
            ),200
        else:
            return json.dumps({'error':'no data'}),500

    else:
        return json.dumps({'error':'no data'}),500