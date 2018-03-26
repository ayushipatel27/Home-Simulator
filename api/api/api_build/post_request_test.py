# importing the requests library
import requests
import json
import datetime

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
 
#r = requests.get('http://127.0.0.1:8000/api/rooms/')

#data = r.json()
 
#data2 = json.dumps(data)

#print("\n" + data2 + "\n")

#url = 'http://127.0.0.1:8000/api/update/'
#payload = [{"roomid":1,"roomname":"Parent Bedroom New"}, {"roomid":2,"roomname":"Child Bedroom 1 New"}, {"roomid":3,"roomname":"Child Bedroom 2 New"}]

#headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#r = requests.post(url, data=json.dumps(payload), headers=headers)



url1 = 'http://127.0.0.1:8000/api/insert/appliances/'

appliances = [{"sensorid":1, "powerusage":12, "powerrate":0.15, "appliancename":"testytesterson"}]

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

req = requests.post(url1, data=json.dumps(appliances), headers=headers)


url2 = 'http://127.0.0.1:8000/api/insert/rooms/'

rooms = [{"roomname":"testytestersonsgarage"}]

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

req = requests.post(url2, data=json.dumps(rooms), headers=headers)


url3 = 'http://127.0.0.1:8000/api/insert/sensors/'

sensors = [{"sensorname":"Light", "sensorstate":0, "roomid":1}, {"sensorname":"Light", "sensorstate":1, "roomid":2}]

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

req = requests.post(url3, data=json.dumps(sensors), headers=headers)



url4 = 'http://127.0.0.1:8000/api/insert/powerusage/'

powerusage = [{"cost":0.585, "endtimestamp": "2015-02-28 10:11:38", "sensorid": 22, "timestamp": "2015-02-28 20:13:56", "usage": 25 }]

req = requests.post(url4, data=json.dumps(powerusage), headers=headers)


url5 = 'http://127.0.0.1:8000/api/insert/hvacusage/'

hvacusage = [{"timestamp":'2015-03-26 12:12:10', "sensorid":2, "endtimestamp":'2015-03-26 19:10:25', "usage":12.0, "cost":12.0, "temperature":65.0}]

req = requests.post(url5, data=json.dumps(hvacusage), headers=headers)


url6 = 'http://127.0.0.1:8000/api/insert/waterusage/'

waterusage = [{"timestamp":'2015-03-26 10:12:10', "sensorid":3, "endtimestamp":'2015-03-26 19:10:25', "usage":12.0, "cost":12.0}]

req = requests.post(url6, data=json.dumps(waterusage), headers=headers)


url7 = 'http://127.0.0.1:8000/api/insert/dailyusage/'

dailyusage = [{"date":"2015-02-23", "totalwaterusage":10.0, "totalpowerusage":75, "totalpowercost":12.0, "totalwatercost":12.0, "totalhvacusage":12.0, "totalhvaccost":12.0}]

req = requests.post(url7, data=json.dumps(dailyusage), headers=headers)




#url = 'http://127.0.0.1:8000/api/updateroom/'
#payload = {"roomid":1,"roomname":"SUCCESS"}
#r = requests.patch(url, data=json.dumps(payload))

#PATCH "http://127.0.0.1:8000/api/rooms/1/"
#{
#    "roomname" : "Parent Bedroom New"
#}

#url = "http://127.0.0.1:8000/api/rooms/1/"
#data = {'roomname' : 'Parent Bedroom New'}
#headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#r = requests.patch(url, data=json.dumps(data), headers=headers)

#http --json PATCH http://127.0.0.1:8000/api/rooms/aa/
#{
#    "roomname" : "Parent Bedroom New"
#}

# instance.roomname = request.data.get("roomname")
#         instance.save()

#         serializer = self.get_serializer(instance)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)

#         return Response(serializer.data)