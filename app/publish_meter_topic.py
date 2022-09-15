from concurrent.futures import thread
import json
from tracemalloc import start
from flask import request,Response,jsonify
import paho.mqtt.client as mqtt
import time

import requests
import threading




def meterpublish(meter):
    

    

    def start_publish(url):
        
        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        res=json.loads(response.content)
   
        mqttBroker = "127.0.0.1"#"mqtt.eclipseprojects.io"
        client = mqtt.Client(res['name'])
        client.connect(mqttBroker)
        b=int(res['recharge_amount'])
        client.publish(str(b))
        #print(json.dumps("Just published " + str(b) + " to Topic " +res['name']))

        url2 = "http://127.0.0.1:5000/v1.0/update_utitlity_meter/"

        payload2 = json.dumps({
            "id": int(res['id']),
            "name": res['name'],
            "image": res['image'],
            "recharge_amount": float(res['recharge_amount'])-1,
            "treshold_amount": res['treshold_amount'],
            "description": res['description']
        })
        headers2 = {
            'Content-Type': 'application/json'
        }
        response2 = requests.request("PUT", url2, headers=headers2, data=payload2)
        print(response2.text)
        time.sleep(10)

    def gen():

        while True:
            url = "http://127.0.0.1:5000/v1.0/utitlity_meter/"+meter
            
            thread=threading.Thread(target=start_publish,args=(url,))
            thread.start()
            #randNumber = uniform(20.0, 21.0)
            #client.publish(res['name'], randNumber)
            #print(json.dumps("Just published " + str(randNumber) + " to Topic " +res['name']))
            time.sleep(1)
    return Response(gen())
 