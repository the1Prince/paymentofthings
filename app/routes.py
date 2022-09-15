from app import app,publish_meter_topic,subscribe_meter_topic
from app.category import addcategory
from app.brand import addbrand
from app.device import adddevice
from app.stock import addstock 
from app.thing import addthing
from app.supplier import addsupplier
from app.orderdetails import addorderdetails
from app.utility_meter import addutility_meter, getutility_meter,update_utility_meter
from flask import jsonify, redirect
from config import Config


@app.route('/')
@app.route('/index', methods=['GET','POST'])
def index():
    return redirect(Config.SWAGGER_URL)


##############################################################
###########brand routes############
@app.route('/v1.0/brand/', methods=['POST'])
def createbrand():
    add=addbrand.addNewBrand()
    return(add)





##############################################################
###########category routes############
@app.route('/v1.0/category/', methods=['POST'])
def createcategory():
    add=addcategory.addNewCategory()
    return(add)




##############################################################
###########device routes############
@app.route('/v1.0/device/', methods=['POST'])
def createdevice():
    add=adddevice.addNewDevice()
    return(add)



##############################################################
###########thing routes############
@app.route('/v1.0/thing/', methods=['POST'])
def creatething():
    add=addthing.addNewThing()
    return(add)



##############################################################
###########supplier routes############
@app.route('/v1.0/supplier/', methods=['POST'])
def createsupplier():
    add=addsupplier.addNewSupplier()
    return(add)


##############################################################
###########stock routes############
@app.route('/v1.0/stock/', methods=['POST'])
def createstock():
    add=addstock.addNewStock()
    return(add)


##############################################################
###########order details routes############
@app.route('/v1.0/orderdetails/', methods=['POST'])
def createorder():
    add=addorderdetails.addNewOrderdetails()
    return(add)

##############################################################
###########utility meter routes############
@app.route('/v1.0/utitlity_meter/', methods=['POST'])
def createutility_meter():
    add=addutility_meter.addNewUtilityMeter()
    return(add)

@app.route('/v1.0/utitlity_meter/<name>/', methods=['GET'])
def get_utility_meter(name):
    getutility=getutility_meter.getutilityMeter(name)
    return(getutility)


@app.route('/v1.0/update_utitlity_meter/', methods=['PUT'])
def updatemeter():
    updatemet=update_utility_meter.updateUtility()
    return(updatemet)


##############################################################
###########publish topic routes############
@app.route('/v1.0/publish_meter_topic/<meter>/', methods=['POST'])
def publish(meter):
    publisht=publish_meter_topic.meterpublish(meter)
    return(publisht)


##############################################################
###########subscribe topic routes############
@app.route('/v1.0/subscribe_meter_topic/<meter>/', methods=['POST'])
def subscribe(meter):
    subscribet=subscribe_meter_topic.metersubscribe(meter)
    return(subscribet)