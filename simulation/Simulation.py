import simpy, random
from datetime import timedelta, time

# Creat Power Usage objects to update power usage tables.
class PowerUsage(object):
    def __init__(self, appliance, startTime, endTime, usage, cost):
        self.appliance = appliance
        self.startTime = startTime
        self.endTime = endTime
        self.usage = usage
        self.cost = cost


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
    def __init__(self, roomName):
        self.roomName = roomName
        self.appliances = []

    def getRoomName(self):
        return self.roomName

    def addAppliance(self, appliance):
        self.appliances.append(appliance)

    def getAppliances(self):
        return self.appliances

    def getApplianceNames(self):
        appliances =""
        for appliance in self.appliances:
            appliances += appliance.getApplianceName() + "\n"
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
                   Sensor("Living Room TV", 0),
                   Sensor("Bedroom TV", 0),
                   Sensor("Exhaust Fan", 0),
                   Sensor("Stove", 0),
                   Sensor("Oven", 0),
                   Sensor("Microwave", 0),
                   Sensor("Refrigerator", 0),
                   Sensor("Dishwasher", 0),
                   Sensor("Clothes Washer", 0),
                   Sensor("Clothes Dryer", 0),
                   Sensor("Hot Water Heater", 0),
                   Sensor("Door", 0),
                   Sensor("Window", 0),
                   Sensor("HVAC", 0)]
        return sensors

    def createAppliances(self, sensors):
        appliances = [Appliance("Overhead Light", sensors[0], 60),
                      Appliance("Lamp", sensors[1], 60),
                      Appliance("Living Room TV", sensors[2], 636),
                      Appliance("Bedroom TV", sensors[3], 636),
                      Appliance("Bath Exhaust Fan", sensors[4], 30),
                      Appliance("Stove", sensors[5], 3500),
                      Appliance("Oven", sensors[6], 4000),
                      Appliance("Microwave", sensors[7], 1100),
                      Appliance("Refrigerator", sensors[8], 150),
                      Appliance("Dishwasher", sensors[9], 1800),
                      Appliance("Clothes Washer", sensors[10], 500),
                      Appliance("Clothes Dryer", sensors[11], 3000),
                      Appliance("Hot Water Heater", sensors[12], 4500),
                      Appliance("Door", sensors[13], 0),
                      Appliance("Window",sensors[14], 0),
                      Appliance("HVAC", sensors[15], 3500)]
        return appliances

    def createRooms(self, appliances):
        rooms = [Room("Bedroom 1"), Room("Bedroom 2"), Room("Bedroom 3"), Room("Bathroom 1"),
                 Room("Bathroom 2"), Room("Garage"), Room("Living Room"), Room("Kitchen"),
                 Room("Laundry Room")]
        # I know this is stupid but it was the only way it was letting me add two of the same appliances.
        # Fix later.
        rooms[0].addAppliance(appliances[0])
        rooms[0].addAppliance(appliances[1])
        rooms[0].addAppliance(appliances[1])
        rooms[0].addAppliance(appliances[3])
        rooms[0].addAppliance(appliances[14])
        rooms[0].addAppliance(appliances[14])
        rooms[1].addAppliance(appliances[0])
        rooms[1].addAppliance(appliances[1])
        rooms[1].addAppliance(appliances[1])
        rooms[1].addAppliance(appliances[3])
        rooms[1].addAppliance(appliances[14])
        rooms[1].addAppliance(appliances[14])
        rooms[2].addAppliance(appliances[0])
        rooms[2].addAppliance(appliances[1])
        rooms[2].addAppliance(appliances[1])
        rooms[2].addAppliance(appliances[3])
        rooms[2].addAppliance(appliances[14])
        rooms[2].addAppliance(appliances[14])
        rooms[3].addAppliance(appliances[0])
        rooms[3].addAppliance(appliances[4])
        rooms[4].addAppliance(appliances[0])
        rooms[4].addAppliance(appliances[4])
        rooms[5].addAppliance(appliances[13])
        rooms[5].addAppliance(appliances[13])
        rooms[5].addAppliance(appliances[14])
        rooms[5].addAppliance(appliances[12])
        rooms[6].addAppliance(appliances[0])
        rooms[6].addAppliance(appliances[1])
        rooms[6].addAppliance(appliances[1])
        rooms[6].addAppliance(appliances[2])
        rooms[6].addAppliance(appliances[13])
        rooms[6].addAppliance(appliances[13])
        rooms[6].addAppliance(appliances[14])
        rooms[6].addAppliance(appliances[14])
        rooms[6].addAppliance(appliances[15])
        rooms[7].addAppliance(appliances[0])
        rooms[7].addAppliance(appliances[5])
        rooms[7].addAppliance(appliances[6])
        rooms[7].addAppliance(appliances[7])
        rooms[7].addAppliance(appliances[8])
        rooms[7].addAppliance(appliances[9])
        rooms[7].addAppliance(appliances[13])
        rooms[8].addAppliance(appliances[10])
        rooms[8].addAppliance(appliances[11])
        return rooms

    def createHome(self, rooms):
        home = Home(rooms, 2, 2)
        return home

    def printHouseDetail(self, home, rooms, appliances, sensors):
        print("Home Detail: \n\nNumber Of Adults: "
              + str(home.getNumOfAdults())
              + "\nNumber of Kids: "
              + str(home.getNumOfKids()) + "\n")

        print("Rooms: \n")
        for room in rooms:
            print("Room name: " + room.getRoomName() + "\n"
                  + "Appliances in room: \n"
                  + room.getApplianceNames() + "\n")

        print("Appliances: \n")
        for appliance in appliances:
            print("Appliance name: " + appliance.getApplianceName() +
                  "\nWatts: " + str(appliance.getWatts()) + "\n")

        print("Each appliance has a sensor of it's own.")

    def calculatePowerCost(self, watts, time):
        return ((watts * time) / 1000) * .12

    def calculatePowerUsage(self, watts, time):
        return (watts * time) / 1000

    def generateRandomTime(self, currentTime):
        while True:
            randomTime = random.randint(currentTime, currentTime+7200)
            if currentTime < randomTime:
                break
        return randomTime - currentTime

    def convertSecondsToTime(self, seconds):
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        if h > 23:
            h = 23
        t = time(h,m,s)
        return t.strftime("%I:%M:%S %p")

    def simulatePowerUsage(self, appliance, probability):
        print("\n" + "Toggling sensors for appliance " + appliance.getApplianceName())
        wakeTime = 18000
        sleepTime = 73800
        totalTimeOn = 0
        totalTime = wakeTime
        while wakeTime <= totalTime <= sleepTime:
            timeOn = random.randint(1, int(sleepTime*probability))
            randomTime = self.generateRandomTime(totalTime)
            totalTime += randomTime + timeOn
            totalTimeOn += timeOn
            appliance.getSensor().setSensorState(1)
            print("Turning on sensor at " + str(self.convertSecondsToTime(totalTime)))

            timeOff = random.randint(1, int(sleepTime*probability))
            randomTime = self.generateRandomTime(totalTime)
            totalTime += randomTime + timeOff
            appliance.getSensor().setSensorState(0)
            print("Turning off sensor at " + str(self.convertSecondsToTime(totalTime)))
        print("Total time on should be " + str(int(sleepTime*probability)) + " but is " + str(totalTimeOn))
        # Time aren't matching for total time to be turned on, check probabilities.



def simulate():
    s = Simulation()

    sensors = s.createSensors()
    appliances = s.createAppliances(sensors)
    rooms = s.createRooms(appliances)
    home = s.createHome(rooms)

    s.printHouseDetail(home, rooms, appliances, sensors)

    days = ["Mon","Tues","Wed","Thurs","Fri","Sat","Sun"]
    dayOfWeek = "Mon"

    print("\nSimulating power usage for appliances in rooms.\n")

    for room in rooms:
        print("\nRoom: " + room.getRoomName())
        for appliance in room.getAppliances():
            if appliance.getApplianceName() == "Overhead Light":
                s.simulatePowerUsage(appliance, 1/10)
            if appliance.getApplianceName() == "Lamp":
                s.simulatePowerUsage(appliance, 1/10)
            if appliance.getApplianceName() == "Living Room TV":
                if dayOfWeek in days[0:5]:
                    s.simulatePowerUsage(appliance, 1/6)
                elif dayOfWeek in days[5:7]:
                    s.simulatePowerUsage(appliance, 1/3)
            if appliance.getApplianceName() == "Bedroom TV":
                if dayOfWeek in days[0:5]:
                    s.simulatePowerUsage(appliance, 1/12)
                elif dayOfWeek in days[5:7]:
                    s.simulatePowerUsage(appliance, 1/6)
            if appliance.getApplianceName() == "Bath Exhaust Fan":
                s.simulatePowerUsage(appliance, 1/5)
            if appliance.getApplianceName() == "Stove":
                if dayOfWeek in days[0:5]:
                    s.simulatePowerUsage(appliance, 1/96)
                elif dayOfWeek in days[5:7]:
                    s.simulatePowerUsage(appliance, 1/48)
            if appliance.getApplianceName() == "Oven":
                if dayOfWeek in days[0:5]:
                    s.simulatePowerUsage(appliance, 1/32)
                elif dayOfWeek in days[5:7]:
                    s.simulatePowerUsage(appliance, 1/24)
            if appliance.getApplianceName() == "Microwave":
                if dayOfWeek in days[0:5]:
                    s.simulatePowerUsage(appliance, 1/72)
                elif dayOfWeek in days[5:7]:
                    s.simulatePowerUsage(appliance, 1/48)
            if appliance.getApplianceName() == "Refrigerator":
                s.simulatePowerUsage(appliance, 1/5)


simulate()








