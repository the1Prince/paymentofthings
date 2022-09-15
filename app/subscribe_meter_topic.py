from concurrent.futures import thread
import json
from flask import request,Response,jsonify
import paho.mqtt.client as mqtt
import time

import requests
import threading
import uuid



def metersubscribe(meter):


    def start_subscribe(url):
            
            payload={}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            res=json.loads(response.content)

            mqttBroker = "127.0.0.1"#"mqtt.eclipseprojects.io"
            client = mqtt.Client(res['name'])
            client.connect(mqttBroker)

            client.loop_start()
            b=int(res['recharge_amount'])
            client.subscribe(str(b))
            client.on_message = start_subscribe

            print(response.text)
            if int(res['recharge_amount']) == int(res['treshold_amount']):
                print('helloo there')
                url2 = "https://sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay"
                x=str(uuid.uuid4())
                print(x)

                payload2 = json.dumps({
                "amount": "50",
                "currency": "EUR",
                "externalId": "123",
                "payer": {
                    "partyIdType": "MSISDN",
                    "partyId": "0545730281"
                },
                "payerMessage": "string",
                "payeeNote": "string"
                })
                headers2 = {
                'X-Reference-Id': x,
                'X-Target-Environment': 'sandbox',
                'Ocp-Apim-Subscription-Key': 'f13cd909d6754665a244365a9a136d96',
                'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSMjU2In0.eyJjbGllbnRJZCI6IjVmYTE4NDkxLTlhMzktNDdiOS05ZjRlLTE5ODE1YjY4MmJiYiIsImV4cGlyZXMiOiIyMDIyLTA5LTE1VDAwOjA3OjE3LjAwNyIsInNlc3Npb25JZCI6Ijg1NzZlYzA4LTAzMWMtNGYyNy1iMzFjLWIwNDMzMGYwNTEyNiJ9.VOEGNUfF8ykktdnRXYqNj26HcrHJKYVa3qtwJt37-4U5l8ZbJvXDtm4w5xDBTxpkW4gl6xanw01YMDffZOHDwBf4NCCdCSGWGQ8r-O4hC2HXX2PK75Dzwjoxkk4xRne0Bh4b_Gq4Ay18g-2EZ1utOOxDoTx6qrLiN2c2AkMbpqLWJ1O1VEzYM2nJ58SzbIDYNKI6EVNrFHtL6EGRT8aajoD5UYYTf82RapMQx7QG7KpMcfqhiFlcd52wMIiiqxLiobLLhrTelWdAMNpqq2kx6K1yMfb3wd9hwuJc9-RYFs2PU2ylfkYWaDIlIRQkmkno3ABeXMeRNgvPflKxuLBEOg',
                'Content-Type': 'application/json'
                }

                payresponse = requests.request("POST", url2, headers=headers2, data=payload2)
                #payres=json.loads(payresponse.content)


                url4 = "http://127.0.0.1:5000/v1.0/update_utitlity_meter/"

                payload4 = json.dumps({
                "id": 1,
                "name": "gh meter",
                "image": "",
                "recharge_amount": "50",
                "treshold_amount": "20",
                "description": ""
                })
                headers4 = {
                    'Content-Type': 'application/json'
                        }
                response = requests.request("PUT", url4, headers=headers4, data=payload4)
                    

                '''if payresponse.ok==True:
                        print('jojo')
                        url3 = "https://sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay/"+x
                        

                    payload3={}
                    headers3 = {
                    'X-Target-Environment': 'sandbox',
                    'Ocp-Apim-Subscription-Key': 'f13cd909d6754665a244365a9a136d96',
                    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSMjU2In0.eyJjbGllbnRJZCI6IjVmYTE4NDkxLTlhMzktNDdiOS05ZjRlLTE5ODE1YjY4MmJiYiIsImV4cGlyZXMiOiIyMDIyLTA5LTE0VDIyOjU5OjAzLjE1MyIsInNlc3Npb25JZCI6Ijk5OGNiZDYxLWJmNzItNDgwMy1hNGIwLTVhMzcwOGI3YjdjYiJ9.MA5R1wfT2d6oTTFSVHXSMEgGkjnuej8no8hWSp5rNoJW7Og1Tl6F4hu9-UTwXcZmdWK0AJqh-3rOuh_Wt8DpHfsUxv7T7DXOqASgg4pw7Hk8Wurf0hXfbovrmTHzZkypJlWURnutuoWHH_26a5gBQda9vtn0w3lifz56WRUdJGuJZ4oxj5MGrpRtYJrng5lVVTmJbH4kTOW3XMm41TyxY-nLHrid62K2D6bpgLDWRmtgbJIuGENX6r37tgRpOtsF_QetxCTu1Mb0KiEXIb4LwK8ER9IF9o3I6bne1izanJOBIfsbkNEZVHSfZ8Bsx8S-gqk0xnOSKkh8iAyCTDZ67w'
                    }
                    paystat = requests.request("GET", url3, headers=headers3, data=payload3)
                    paystatus=json.loads(paystat.content)

                    if paystatus['status']=="SUCCESSFUL":
                        url4 = "http://127.0.0.1:5000/v1.0/update_utitlity_meter/"

                        payload4 = json.dumps({
                        "id": 1,
                        "name": "gh meter",
                        "image": "",
                        "recharge_amount": "50",
                        "treshold_amount": "7",
                        "description": ""
                        })
                        headers4 = {
                        'Content-Type': 'application/json'
                        }
                        response = requests.request("PUT", url4, headers=headers4, data=payload4)
                else:
                    print(payresponse.content) '''     


           

    def sub():

        while True:
            url = "http://127.0.0.1:5000/v1.0/utitlity_meter/"+meter
            
            thread=threading.Thread(target=start_subscribe,args=(url,))
            thread.start()
            time.sleep(1)
                    
                    
            
    return jsonify(Response(sub()))


    