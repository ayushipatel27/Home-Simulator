import simpy, random
from datetime import timedelta, time

class PowerUsage(object):
    def __init__(self, sensor, startTime, endTime, usage, cost):
        self.sensor = sensor
        self.startTime = startTime
        self.endTime = endTime
        self.usage = usage
        self.cost = cost

class HvacUsage(object):
    def __init__(self, sensor, startTime, endTime, temperature, usage, cost):
        self.sensor = sensor
        self.startTime = startTime
        self.endTime = endTime
        self.temperature = temperature
        self.usage = usage
        self.cost = cost

class WaterUsage(object):
    def __init__(self, sensor, startTime, endTime, usage, cost):
        self.sensor = sensor
        self.startTime = startTime
        self.endTime = endTime
        self.usage = usage
        self.cost = cost

class DailyUsage(object):
    def __init__(self, date, totalWaterUsage, totalPowerUsage, totalHvacUsage, totalPowerCost, totalWaterCost, totalHvacCost):
        self.date = date
        self.totalWaterUsage = totalWaterUsage
        self.totalPowerUsage = totalPowerUsage
        self.totalHvacUsage = totalHvacUsage
        self.totalWaterCost = totalWaterCost
        self.totalPowerCost = totalPowerCost
        self.totalHvacCost = totalHvacCost

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

    def addAppliances(self, appliances):
        for appliance in appliances:
            for i in range(appliances[appliance]):
                self.appliances.append(appliance)

    def getAppliances(self):
        return self.appliances

    def getApplianceNames(self):
        appliances =""
        for appliance in self.appliances:
            appliances += appliance.getApplianceName() + "\t"
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
        self.sensors = []
        self.appliances = []
        self.rooms = []
        self.powerUsages = []
        self.waterUsages = []
        self.HvacUsages = []
        self.dailyUsages = []

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
                   Sensor("Hvac", 0),
                   Sensor("Bath", 0),
                   Sensor("Shower", 0)]

        self.sensors = sensors
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
                      Appliance("Hvac", sensors[15], 3500),
                      Appliance("Bath", sensors[16], 0),
                      Appliance("Shower", sensors[17], 0)]

        self.appliances = appliances
        return appliances

    def createRooms(self, appliances):
        rooms = [Room("Bedroom 1"), Room("Bedroom 2"), Room("Bedroom 3"), Room("Bathroom 1"),
                 Room("Bathroom 2"), Room("Garage"), Room("Living Room"), Room("Kitchen"),
                 Room("Laundry Room")]

        rooms[0].addAppliances({appliances[0]: 1, appliances[1]: 2, appliances[3]: 1, appliances[14]: 2})
        for room in rooms[1:3]:
            room.addAppliances({appliances[0]: 1, appliances[1]: 2, appliances[14]: 2})
        for room in rooms[3:5]:
            room.addAppliances({appliances[0]: 1, appliances[4]: 1})
        rooms[5].addAppliances({appliances[13]: 2, appliances[14]: 1, appliances[12]: 1})
        rooms[6].addAppliances({appliances[0]: 1, appliances[1]: 2, appliances[2]: 1, appliances[13]: 2, appliances[14]: 2, appliances[15]: 1})
        rooms[7].addAppliances({appliances[0]: 1, appliances[5]: 1, appliances[6]: 1, appliances[7]: 1, appliances[8]: 1, appliances[9]: 1, appliances[13]: 1})
        rooms[8].addAppliances({appliances[10]: 1, appliances[11]: 1})

        self.rooms = rooms
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
                  + "Appliances: "
                  + room.getApplianceNames() + "\n")

        print("Appliances: \n")
        for appliance in appliances:
            print("Appliance name: " + appliance.getApplianceName() +
                  "\tWatts: " + str(appliance.getWatts()) + "\n")

        print("Each appliance has a sensor of it's own.")

    def updatePowerUsage(self, sensor, startTime, endTime, usage, cost):
        self.powerUsages.append(PowerUsage(sensor, startTime, endTime, usage, cost))

    def updateWaterUsage(self, sensor, startTime, endTime, usage, cost):
        self.powerUsages.append(WaterUsage(sensor, startTime, endTime, usage, cost))

    def updateHvacUsage(self, sensor, startTime, endTime, temperature, usage, cost):
        self.powerUsages.append(HvacUsage(sensor, startTime, endTime, usage, cost))

    def updateDailyUsage(self,  date, totalWaterUsage, totalPowerUsage, totalHvacUsage, totalPowerCost, totalWaterCost, totalHvacCost):
        self.dailyUsages.append(DailyUsage( date, totalWaterUsage, totalPowerUsage, totalHvacUsage, totalPowerCost, totalWaterCost, totalHvacCost))

    def updateSensors(self, name, state):
        self.sensors.append(Sensor(name, state))

    def isWeekday(self, day):
        days = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]
        if day in days[0:5]:
            return True
        elif day in days[5:7]:
            return False

    def getTimeOn(self, appliance, day):
        time = 0
        if appliance.getApplianceName() == "Overhead Light":
            if self.isWeekday(day):
                time = random.randint(1, 25200)
            else:
                time = random.randint(1, 25200)
        if appliance.getApplianceName()  == "Lamp":
            if self.isWeekday(day):
                time = random.randint(1, 25200)
            else:
                time = random.randint(1,25200)
        if appliance.getApplianceName()  == "Living Room TV":
            if self.isWeekday(day):
                time = 14400
            else:
                time = 28800
        if appliance.getApplianceName()  == "Bedroom TV":
            if self.isWeekday(day):
                time = 7200
            else:
                time = 14400
        if appliance.getApplianceName()  == "Bath Exhaust Fan":
            if self.isWeekday(day):
                time = random.randint(1, 3600)
            else:
                time = random.randint(1,7200)
        if appliance.getApplianceName()  == "Stove":
            if self.isWeekday(day):
                time = 900
            else:
                time = 1800
        if appliance.getApplianceName()  == "Oven":
            if self.isWeekday(day):
                time = 2700
            else:
                time = 3600
        if appliance.getApplianceName()  == "Microwave":
            if self.isWeekday(day):
                time = 1200
            else:
                time = 1800
        if appliance.getApplianceName()  == "Refrigerator":
            if self.isWeekday(day):
                time = random.randint(1, 3600)
            else:
                time = random.randint(1,7200)
        return time

    def calculatePowerCost(self, watts, time):
        return (watts * (time/3600)) * .12

    def calculatePowerUsage(self, watts, time):
        return watts * (time/3600)


    def simulatePowerUsage(self, appliance, day):

        wakeTime = 18000  # 5:00 AM
        leaveTime = 27000  # 7:30 AM
        comeHomeTime = 57600  # 4:00 PM
        sleepTime = 73800  # 10:30 PM
        totalTime = wakeTime
        totalUsage = 0
        totalCost = 0


        print("Total Usage: %.2f watts" % (totalUsage))
        print("Total Cost: $%.2f" % (totalCost))


def simulate():
    s = Simulation()

    sensors = s.createSensors()
    appliances = s.createAppliances(sensors)
    rooms = s.createRooms(appliances)
    home = s.createHome(rooms)

    s.printHouseDetail(home, rooms, appliances, sensors)

    print("\nSimulating power usage for appliances in rooms.\n")


simulate()








