import random

class Usage(object):
    def __init__(self, appliance, startTime, endTime):
        self.appliance = Appliance
        self.startTime = startTime
        self.endTime = endTime

    def getStartTime(self):
        return self.startTime

    def getEndTime(self):
        return self.endTime

    def setStartTime(self, startTime):
        self.startTime = startTime

    def setEndTime(self, endTime):
        self.endTime = endTime

class PowerUsage(Usage):
    def __init__(self, cost, appliance, startTime, endTime):
        self.cost = cost
        Usage.__init__(self, appliance, startTime, endTime)

class HVACUsage(Usage):
    def __init__(self, internalTemp, externalTemp, desiredTemp, appliance, startTime, endTime):
        self.internalTemp = internalTemp
        self.externalTemp = externalTemp
        self.desiredTemp = desiredTemp
        Usage.__init__(self, startTime, endTime)


class WaterUsage(Usage):
    def __init__(self, gallons, hotWater, coldWater, appliance, startTime, endTime):
        self.gallons = gallons
        self.hotWater = hotWater
        self.coldWater = coldWater
        Usage.__init__(self, appliance, startTime, endTime)

class Sensor(object):
    def __init__(self, sensorName, sensorState):
        self.sensorName = sensorName
        self.sensorState = sensorState

    def getSensorName(self):
        return self.sensorName

    def getSensorState(self):
        return self.sensorState

    def setSensorName(self, sensorName):
        self.sensorName = sensorName

    def setSensorState(self, sensorState):
        self.sensorState = sensorState

class Appliance(object):
    def __init__(self, sensor, watts, quantity):
        self.sensor = sensor
        self.watts = watts
        self.quantity = quantity

    def getSensor(self):
        return self.sensor

    def getWatts(self):
        return self.watts

    def getQuantity(self):
        return self.quantity

    def setSensor(self, sensor):
        self.sensor = sensor

    def setWatts(self, watts):
        self.watts = watts

    def setQuantity(self, quantity):
        self.quantity = quantity

class Room(object):
    def __init__(self, roomName, numOfRooms):
        self.roomName = roomName
        self.numOfRooms = numOfRooms

    def getRoomName(self):
        return self.roomName

    def setRoomname(self, roomName):
        self.roomName = roomName

    def getNumOfRooms(self):
        return self.numOfRooms

    def setNumOfRooms(self, numOfRooms):
        self.numOfRooms = numOfRooms


class Home(object):
    def __init__(self, rooms, numOfAdults, numOfKids):
        self.rooms = rooms
        self.numOfAdults = numOfAdults
        self.numOfKids = numOfKids

    def getRooms(self):
        return self.rooms

    def getNumOfAdults(self):
        return self.numOfAdults

    def getNumOfKids(self):
        return self.numOfKids

    def setRooms(self, rooms):
        self.rooms = rooms

    def setNumOfAdults(self, numOfAdults):
        self.numOfAdults = numOfAdults

    def setNumOfKids(self, numOfKids):
        self.numOfKids = numOfKids


class Simulation(object):
    def __init__(self):
        self.home = Home

    def createSensors(self):
        sensors = [Sensor("Overhead Light", 0),
                   Sensor("Lamp", 0),
                   Sensor("TV", 0),
                   Sensor("Exhaust Fan", 0),
                   Sensor("Stove", 0),
                   Sensor("Oven", 0),
                   Sensor("Microwave", 0),
                   Sensor("Refrigerator", 0),
                   Sensor("Dishwasher", 0),
                   Sensor("Clothes Washer", 0),
                   Sensor("Clothes Dryer", 0),
                   Sensor("Door", 0),
                   Sensor("Window", 0)]
        return sensors

    def createAppliances(self, sensors):
        appliances = [Appliance(sensors[0], 60, 4),
                      Appliance(sensors[1], 60, 4),
                      Appliance(sensors[2], 636, 2),
                      Appliance(sensors[3], 30, 1),
                      Appliance(sensors[4], 3500, 1),
                      Appliance(sensors[5], 4000, 1),
                      Appliance(sensors[6], 1100, 1),
                      Appliance(sensors[7], 150, 1),
                      Appliance(sensors[8], 1800, 1),
                      Appliance(sensors[9], 500, 1),
                      Appliance(sensors[10], 3000, 1),
                      Appliance(sensors[11], 0, 5),
                      Appliance(sensors[12], 0, 6)]
        return appliances

    def createRooms(self):
        rooms = [Room("Bedroom", 3),
                 Room("Bathroom", 2),
                 Room("Garage", 2),
                 Room("Living Room", 1),
                 Room("Kitchen", 1)]
        return rooms

    def createHome(self, rooms):
        home = Home(rooms, 2, 2)
        return home

def simulate():
    s = Simulation()

    sensors = s.createSensors()
    appliances = s.createAppliances(sensors)
    rooms = s.createRooms()
    home = s.createHome(rooms)

    print("Home Detail: \n\nNumber Of Adults: " + str(home.getNumOfAdults())
          + "\nNumber of Kids: " + str(home.getNumOfKids()) + "\n")

    print("Rooms\n")
    for room in rooms:
        print("Room name: " + room.getRoomName() + "\nNumber of Room: "
              + str(room.getNumOfRooms()) + "\n")

    print("Appliances\n")
    for appliance in appliances:
        print("Appliance name: " + appliance.getSensor().getSensorName() +
              "\nWatts: " + str(appliance.getWatts()) +
              "\nQuantity: " + str(appliance.getQuantity()) + "\n")

    print("Sensors\n")
    for sensor in sensors:
        print("Sensor name: " + sensor.getSensorName() +
              "\nSensor state: " + str(sensor.getSensorState()) + "\n")


simulate()







