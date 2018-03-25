# importing the requests library
import requests
import json
 
#r = requests.get('http://127.0.0.1:8000/api/rooms/')

#data = r.json()
 
#data2 = json.dumps(data)

#print("\n" + data2 + "\n")

#url = 'http://127.0.0.1:8000/api/update/'
#payload = [{"roomid":1,"roomname":"Parent Bedroom New"}, {"roomid":2,"roomname":"Child Bedroom 1 New"}, {"roomid":3,"roomname":"Child Bedroom 2 New"}]

#headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#r = requests.post(url, data=json.dumps(payload), headers=headers)



url1 = 'http://127.0.0.1:8000/api/insert/appliances/'

appliances = [{"sensorid":1, "powerusage":12, "powerrate":0.15}, {"sensorid":2, "powerusage":25, "powerrate":0.15}] #, "appliancename":"Washer"}

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

req = requests.post(url1, data=json.dumps(appliances), headers=headers)


url2 = 'http://127.0.0.1:8000/api/insert/rooms/'

rooms = [{"roomname":"GARAGE"}]

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

req = requests.post(url2, data=json.dumps(rooms), headers=headers)


url3 = 'http://127.0.0.1:8000/api/insert/sensors/'

sensors = [{"sensorname":"Light", "sensorstate":0, "roomid":1}, {"sensorname":"Light", "sensorstate":1, "roomid":2}]

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

req = requests.post(url3, data=json.dumps(sensors), headers=headers)


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