from flask import jsonify
from app.models import Utility_meter


def getutilityMeter(name):
    '''get a single utility meter'''
    utility=Utility_meter.query.filter_by(name=name).first()
    if utility:
        return jsonify({'id':utility.id,'name':utility.name,'image':utility.image,'recharge_amount':utility.recharge_amount,'treshold_amount':utility.treshold_amount,'description':utility.description}),201
    else:
        return jsonify({"error":"no record"}),500
    