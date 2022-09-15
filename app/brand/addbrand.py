import json
from app.models import Brand
from app import db
import uuid
from flask import request, jsonify


def addNewBrand():
    '''create a new brand item'''
    data = request.get_json()

    if data and data is not None:
        name=data['name']
        description=data['description']
        logo=data['logo']


        brand=Brand(
            name=name,
            description=description,
            logo=logo

        )
        db.session.add(brand)
        db.session.commit()


        return json.dumps({
            'id':brand.id,'name':brand.name,'description':brand.description,'logo':brand.logo
        },sort_keys=True, indent=4, default=str
        )
        

        