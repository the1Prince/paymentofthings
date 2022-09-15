import json
from app.models import Category
from app import db
import uuid
from flask import request, jsonify


def addNewCategory():
    '''create a new category item'''
    data = request.get_json()

    if data and data is not None:
        name=data['name']
        description=data['description']
        image=data['image']


        category=Category(
            name=name,
            description=description,
            image=image

        )
        db.session.add(category)
        db.session.commit()


        return json.dumps({
            'id':category.id,'name':category.name,'description':category.description,'image':category.image
        },sort_keys=True, indent=4, default=str
        )
        

        