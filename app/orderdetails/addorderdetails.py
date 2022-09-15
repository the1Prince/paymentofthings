import json
from app.models import Order_details
from app import db
import uuid
from flask import request, jsonify


def addNewOrderdetails():
    '''create a new order details'''
    data = request.get_json()

    if data and data is not None:
        stock_id=data['stock_id']
        quantity=data['quantity']
        total_cost=data['total_cost']
        cur_status=data['cur_status']
        description=data['description']
        
       


        orderdetails=Order_details(
            stock_id=stock_id,
            quantity=quantity,
            total_cost=total_cost,
            cur_status=cur_status,
            description=description,
            

        )
        db.session.add(orderdetails)
        db.session.commit()


        return json.dumps({
            'id':orderdetails.id,'stock_id':orderdetails.stock_id,'quantity':orderdetails.quantity,'total_cost':orderdetails.total_cost,'cur_status':orderdetails.cur_status,'description':orderdetails.description
        },sort_keys=True, indent=4, default=str
        
        )
        

        