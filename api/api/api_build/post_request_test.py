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



# url1 = 'http://127.0.0.1:8000/api/insert/appliances/'

# appliances = [{"sensorid":1, "powerusage":12, "powerrate":0.15, "appliancename":"testytesterson"}]

# headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

# req = requests.post(url1, data=json.dumps(appliances), headers=headers)


# url2 = 'http://127.0.0.1:8000/api/insert/rooms/'

# rooms = [{"roomname":"testytestersonsgarage"}]

# headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

# req = requests.post(url2, data=json.dumps(rooms), headers=headers)


# url3 = 'http://127.0.0.1:8000/api/insert/sensors/'

# sensors = [{"sensorname":"Light", "sensorstate":0, "roomid":1}, {"sensorname":"Light", "sensorstate":1, "roomid":2}]

# headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

# req = requests.post(url3, data=json.dumps(sensors), headers=headers)



# url4 = 'http://127.0.0.1:8000/api/insert/powerusagenoendtime/'

# powerusage = [{"timestamp":'2018-03-26 12:12:10', "cost":0.585, "sensorid": 22, "usage": 25 }]

# req = requests.post(url4, data=json.dumps(powerusage), headers=headers)


# url5 = 'http://127.0.0.1:8000/api/insert/hvacusage/'

# hvacusage = [{"timestamp":'2018-03-28 12:12:10', "sensorid":2, "usage":50.0,"endtimestamp":'2018-03-28 12:54:10', "cost":12.0, "temperature":65.0}]

# req = requests.post(url5, data=json.dumps(hvacusage), headers=headers)


# url6 = 'http://127.0.0.1:8000/api/insert/waterusagenoendtime/'

# waterusage = [{"timestamp":'2018-03-27 10:12:10', "sensorid":1, "usage":12.0, "cost":12.0}, {"timestamp":'2018-03-27 11:12:10', "sensorid":2, "usage":12.0, "cost":12.0}]

# req = requests.post(url6, data=json.dumps(waterusage), headers=headers)


# url7 = 'http://127.0.0.1:8000/api/insert/dailyusage/'

# dailyusage = [{"date":"2015-02-23", "totalwaterusage":10.0, "totalpowerusage":75, "totalpowercost":12.0, "totalwatercost":12.0, "totalhvacusage":12.0, "totalhvaccost":12.0}]

# req = requests.post(url7, data=json.dumps(dailyusage), headers=headers)




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








# print(str(HouseState['home']['dailyusage']['totalwaterusage']))

#     for room_key, room_elem in HouseState['home']['rooms'].items():

#         for sensor_key, sensor_elem in room_elem['sensors'].items():

#             dbSensor = Sensors.objects.get(sensorid = sensor_elem['sensor id'])
#             sensor_elem['state'] = dbSensor.sensorstate

#             for appliance_key, appliance_elem in sensor_elem['appliances'].items():

#                     dbAppliance = Appliances.objects.get(applianceid = sensor_elem['sensor id'])
#                     appliance_elem['usage'] = dbAppliance.powerusage

#     # CALCULATE DAILY USAGE

#     dailyusage = Dailyusage.objects.latest('dailyusageid')

#     HouseState['home']['dailyusage']['date']            = dailyusage.date

#     HouseState['home']['dailyusage']['totalpowerusage'] = Powerusage.objects.filter(endtimestamp__isnull=False, timestamp__date=date.today()).aggregate(Sum('usage'))['usage__sum']
#     HouseState['home']['dailyusage']['totalwaterusage'] = Waterusage.objects.filter(endtimestamp__isnull=False, timestamp__date=date.today()).aggregate(Sum('usage'))['usage__sum']
#     HouseState['home']['dailyusage']['totalhvacusage']  = Hvacusage.objects.filter(endtimestamp__isnull=False, timestamp__date=date.today()).aggregate(Sum('usage'))['usage__sum']

#     HouseState['home']['dailyusage']['totalpowercost']  = HouseState['home']['dailyusage']['totalpowerusage'] * 0.12
#     HouseState['home']['dailyusage']['totalwatercost']  = HouseState['home']['dailyusage']['totalwaterusage'] * 0.12
#     HouseState['home']['dailyusage']['totalhvaccost']   = HouseState['home']['dailyusage']['totalhvacusage'] * 0.12

#     # GET CURRENTLY ACTIVE POWER, WATER, AND HVAC 
#     data = serializers.serialize('json', Powerusage.objects.filter(endtimestamp__isnull=True))
#     powerusage = json.loads(data)

#     data = serializers.serialize('json', Hvacusage.objects.filter(endtimestamp__isnull=True))
#     hvacusage = json.loads(data)

#     data = serializers.serialize('json', Waterusage.objects.filter(endtimestamp__isnull=True))
#     waterusage = json.loads(data)

#     HouseState['home']['hvacusage']  = hvacusage
#     HouseState['home']['waterusage'] = waterusage
#     HouseState['home']['powerusage'] = powerusage

#     #payload = json.dumps(HouseState)



payload = {
    "home": {
        "hvacusage": {
            "hvacusage": {
            "cost": 7.5,
            "endtimestamp": "2018-04-01 12:20:10",
            "temperature": 68.0,
            "timestamp": "2018-04-01 12:12:10",
            "usage": 50.0,
            "sensorid": "[]",
            },
        },
        "powerusage": {
            "cost": 9.0,
            "endtimestamp": "2018-03-31 10:29:11",
            "sensorids": "[13,17,37]",
            "timestamp": "2018-03-31 10:13:10",
            "usage": 60.0
        },
        "rooms": {
            "Garage": {
                "sensors": {
                    "Window 1 sensor": {
                        "appliances": {
                            "Window 1": {
                                "usage": 0
                            }
                        },
                        "sensor id": 27,
                        "state": 0
                    },
                    "garage door 1 sensor": {
                        "appliances": {
                            "Garage Door 1": {
                                "usage": 0
                            }
                        },
                        "sensor id": 25,
                        "state": 0
                    },
                    "garage door 2 sensor": {
                        "appliances": {
                            "Garage Door 2": {
                                "usage": 0
                            }
                        },
                        "sensor id": 26,
                        "state": 0
                    },
                    "hot water heater sensor": {
                        "appliances": {
                            "Hot Water Heater": {
                                "usage": 4500
                            }
                        },
                        "sensor id": 28,
                        "state": 0
                    }
                }
            },
            "Kid 1 Bedroom": {
                "sensors": {
                    "Window 2 sensor": {
                        "appliances": {
                            "Window 2": {
                                "usage": 0
                            }
                        },
                        "sensor id": 11,
                        "state": 0
                    },
                    "lamp 1 sensor": {
                        "appliances": {
                            "Lamp 1": {
                                "usage": 60
                            }
                        },
                        "sensor id": 8,
                        "state": 0
                    },
                    "lamp 2 sensor": {
                        "appliances": {
                            "Lamp 2": {
                                "usage": 60
                            }
                        },
                        "sensor id": 9,
                        "state": 0
                    },
                    "overhead light sensor": {
                        "appliances": {
                            "Overhead Light": {
                                "usage": 60
                            }
                        },
                        "sensor id": 7,
                        "state": 0
                    },
                    "window 1 sensor": {
                        "appliances": {
                            "Window 1": {
                                "usage": 0
                            }
                        },
                        "sensor id": 10,
                        "state": 0
                    }
                }
            },
            "Kid 2 Bedroom": {
                "sensors": {
                    "Window 2 sensor": {
                        "appliances": {
                            "Window 2": {
                                "usage": 0
                            }
                        },
                        "sensor id": 16,
                        "state": 0
                    },
                    "lamp 1 sensor": {
                        "appliances": {
                            "Lamp 1": {
                                "usage": 60
                            }
                        },
                        "sensor id": 13,
                        "state": 0
                    },
                    "lamp 2 sensor": {
                        "appliances": {
                            "Lamp 2": {
                                "usage": 60
                            }
                        },
                        "sensor id": 14,
                        "state": 0
                    },
                    "overhead light sensor": {
                        "appliances": {
                            "Overhead Light": {
                                "usage": 60
                            }
                        },
                        "sensor id": 12,
                        "state": 0
                    },
                    "window 1 sensor": {
                        "appliances": {
                            "Window 1": {
                                "usage": 0
                            }
                        },
                        "sensor id": 15,
                        "state": 0
                    }
                }
            },
            "Kids Bathroom": {
                "sensors": {
                    "bath exhaust fan sensor": {
                        "appliances": {
                            "Bath Exhaust Fan": {
                                "usage": 30
                            }
                        },
                        "sensor id": 22,
                        "state": 0
                    },
                    "bath sensor": {
                        "appliances": {
                            "Bath": {
                                "usage": 0
                            }
                        },
                        "sensor id": 23,
                        "state": 0
                    },
                    "overhead light sensor": {
                        "appliances": {
                            "Overhead Light": {
                                "usage": 60
                            }
                        },
                        "sensor id": 21,
                        "state": 0
                    },
                    "shower sensor": {
                        "appliances": {
                            "Shower": {
                                "usage": 0
                            }
                        },
                        "sensor id": 24,
                        "state": 0
                    }
                }
            },
            "Kitchen": {
                "sensors": {
                    "dishwasher sensor": {
                        "appliances": {
                            "Dishwasher": {
                                "usage": 1800
                            }
                        },
                        "sensor id": 42,
                        "state": 0
                    },
                    "garage door into home sensor": {
                        "appliances": {
                            "Garage Door Into Home": {
                                "usage": 0
                            }
                        },
                        "sensor id": 43,
                        "state": 0
                    },
                    "microwave sensor": {
                        "appliances": {
                            "Microwave": {
                                "usage": 1100
                            }
                        },
                        "sensor id": 40,
                        "state": 0
                    },
                    "oven sensor": {
                        "appliances": {
                            "Oven": {
                                "usage": 4000
                            }
                        },
                        "sensor id": 39,
                        "state": 0
                    },
                    "overhead light sensor": {
                        "appliances": {
                            "Overhead Light": {
                                "usage": 60
                            }
                        },
                        "sensor id": 37,
                        "state": 0
                    },
                    "refrigerator sensor": {
                        "appliances": {
                            "Refrigerator": {
                                "usage": 150
                            }
                        },
                        "sensor id": 41,
                        "state": 0
                    },
                    "stove sensor": {
                        "appliances": {
                            "Stove": {
                                "usage": 3500
                            }
                        },
                        "sensor id": 38,
                        "state": 0
                    }
                }
            },
            "Laundry Room": {
                "sensors": {
                    "clothes dryer sensor": {
                        "appliances": {
                            "Clothes Dryer": {
                                "usage": 3000
                            }
                        },
                        "sensor id": 45,
                        "state": 0
                    },
                    "clothes washer sensor": {
                        "appliances": {
                            "Clothes Washer": {
                                "usage": 500
                            }
                        },
                        "sensor id": 44,
                        "state": 0
                    }
                }
            },
            "Living Room": {
                "sensors": {
                    "Window 2 sensor": {
                        "appliances": {
                            "Window 2": {
                                "usage": 0
                            }
                        },
                        "sensor id": 35,
                        "state": 0
                    },
                    "back door sensor": {
                        "appliances": {
                            "Back Door": {
                                "usage": 0
                            }
                        },
                        "sensor id": 32,
                        "state": 0
                    },
                    "front door sensor": {
                        "appliances": {
                            "Front Door": {
                                "usage": 0
                            }
                        },
                        "sensor id": 33,
                        "state": 0
                    },
                    "hvac sensor": {
                        "appliances": {
                            "Hvac": {
                                "usage": 3500
                            }
                        },
                        "sensor id": 36,
                        "state": 0
                    },
                    "lamp sensor": {
                        "appliances": {
                            "Lamp": {
                                "usage": 60
                            }
                        },
                        "sensor id": 30,
                        "state": 0
                    },
                    "living room tv sensor": {
                        "appliances": {
                            "Living Room TV": {
                                "usage": 636
                            }
                        },
                        "sensor id": 31,
                        "state": 0
                    },
                    "overhead light sensor": {
                        "appliances": {
                            "Overhead Light": {
                                "usage": 60
                            }
                        },
                        "sensor id": 29,
                        "state": 0
                    },
                    "window 1 sensor": {
                        "appliances": {
                            "Window 1": {
                                "usage": 0
                            }
                        },
                        "sensor id": 34,
                        "state": 0
                    }
                }
            },
            "Master Bathroom": {
                "sensors": {
                    "bath exhaust fan sensor": {
                        "appliances": {
                            "Bath Exhaust Fan": {
                                "usage": 30
                            }
                        },
                        "sensor id": 18,
                        "state": 0
                    },
                    "bath sensor": {
                        "appliances": {
                            "Bath": {
                                "usage": 0
                            }
                        },
                        "sensor id": 19,
                        "state": 0
                    },
                    "overhead light sensor": {
                        "appliances": {
                            "Overhead Light": {
                                "usage": 60
                            }
                        },
                        "sensor id": 17,
                        "state": 0
                    },
                    "shower sensor": {
                        "appliances": {
                            "Shower": {
                                "usage": 0
                            }
                        },
                        "sensor id": 20,
                        "state": 0
                    }
                }
            },
            "master bedroom": {
                "sensors": {
                    "Window 2 sensor": {
                        "appliances": {
                            "Window 2": {
                                "usage": 0
                            }
                        },
                        "sensor id": 6,
                        "state": 1
                    },
                    "bedroom tv sensor": {
                        "appliances": {
                            "Bedroom TV": {
                                "usage": 636
                            }
                        },
                        "sensor id": 4,
                        "state": 1
                    },
                    "lamp 1 sensor": {
                        "appliances": {
                            "Lamp 1": {
                                "usage": 60
                            }
                        },
                        "sensor id": 2,
                        "state": 1
                    },
                    "lamp 2 sensor": {
                        "appliances": {
                            "Lamp 2": {
                                "usage": 60
                            }
                        },
                        "sensor id": 3,
                        "state": 1
                    },
                    "overhead light sensor": {
                        "appliances": {
                            "Overhead Light": {
                                "usage": 60
                            }
                        },
                        "sensor id": 1,
                        "state": 1
                    },
                    "window 1 sensor": {
                        "appliances": {
                            "Window 1": {
                                "usage": 0
                            }
                        },
                        "sensor id": 5,
                        "state": 1
                    }
                }
            }
        },
        "waterusage": {
            "cost": 11.25,
            "endtimestamp": "2018-03-31 11:53:11",
            "sensorids": "[20,19,44]",
            "timestamp": "2018-03-31 12:35:11",
            "usage": 75
        },
        "weather": {
            "chanceofprecipitation": 30.0,
            "precipitation": 20.0,
            "state": "Sunny",
            "temperature": 65.0,
            "timestamp": "2018-04-01T19:46:49"
        }
    }
}

url = 'http://127.0.0.1:8000/api/update/housestate/'

r = requests.post(url, data=json.dumps(payload), headers=headers)


