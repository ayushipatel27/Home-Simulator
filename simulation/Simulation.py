class Sensor(object):
    def __init__(self, sensorName, sensorState):
        self.sensorName = sensorName
        self.sensorState = sensorState

    def getSensorName(self):
        return self.sensorName

    def getSensorState(self):
        return self.sensorState

    def setSensorState(self, sensorState):
        self.sensorState = sensorState

class Appliance(object):
    def __init__(self, applianceName, sensor, watts):
        self.applianceName = applianceName
        self.sensor = sensor
        self.watts = watts

    def getApplianceName(self):
        return self.applianceName

    def getSensor(self):
        return self.sensor

    def getWatts(self):
        return self.watts


class Room(object):
    def __init__(self, roomName, numOfRooms, appliances):
        self.roomName = roomName
        self.numOfRooms = numOfRooms
        self.appliances = appliances

    def getRoomName(self):
        return self.roomName

    def getNumOfRooms(self):
        return self.numOfRooms

    def getAppliances(self):
        appliances = ""
        for appliance in self.appliances:
            appliances = appliances + "\n\tAppliance: " + appliance.applianceName + "\t Quantity: " + str(self.appliances[appliance])
        return appliances


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
        appliances = [Appliance("Overhead Light", sensors[0], 60),
                      Appliance("Lamp", sensors[1], 60),
                      Appliance("TV", sensors[2], 636),
                      Appliance("Exhaust Fan", sensors[3], 30),
                      Appliance("Stove", sensors[4], 3500),
                      Appliance("Oven", sensors[5], 4000),
                      Appliance("Microwave", sensors[6], 1100),
                      Appliance("Refrigerator", sensors[7], 150),
                      Appliance("Dishwasher", sensors[8], 1800),
                      Appliance("Clothes Washer", sensors[9], 500),
                      Appliance("Clothes Dryer", sensors[10], 3000),
                      Appliance("Door", sensors[11], 0),
                      Appliance("Window",sensors[12], 0)]
        return appliances

    def createRooms(self, appliances):
        rooms = [Room("Bedroom", 3, {appliances[0]: 1, appliances[1]: 2, appliances[2]: 1, appliances[12]: 2}),
                 Room("Bathroom", 2, {appliances[0]: 1, appliances[3]: 1}),
                 Room("Garage", 2, {appliances[11]: 2, appliances[12]: 2}),
                 Room("Living Room", 1, {appliances[0]: 1, appliances[1]: 2, appliances[2]: 1,
                                         appliances[11]: 2, appliances[12]: 2}),
                 Room("Kitchen", 1, {appliances[0]: 1, appliances[4]: 1, appliances[5]: 1, appliances[6]: 1,
                                     appliances[7]: 1,  appliances[8]: 1, appliances[11]: 1})]
        return rooms

    def createHome(self, rooms):
        home = Home(rooms, 2, 2)
        return home

def simulate():
    s = Simulation()

    sensors = s.createSensors()
    appliances = s.createAppliances(sensors)
    rooms = s.createRooms(appliances)
    home = s.createHome(rooms)

    print("Home Detail: \n\nNumber Of Adults: "
          + str(home.getNumOfAdults())
          + "\nNumber of Kids: "
          + str(home.getNumOfKids()) + "\n")

    print("Rooms\n")
    for room in rooms:
        print("Room name: " + room.getRoomName()
              + "\nNumber of " + room.getRoomName() + "s: "
              + str(room.getNumOfRooms())
              + str(room.getAppliances()) + "\n")

    print("Appliances\n")
    for appliance in appliances:
        print("Appliance name: " + appliance.getSensor().getSensorName() +
              "\nWatts: " + str(appliance.getWatts()) + "\n")

    print("Sensors\n")
    for sensor in sensors:
        print("Sensor name: " + sensor.getSensorName() +
              "\nSensor state: " + str(sensor.getSensorState()) + "\n")


simulate()







