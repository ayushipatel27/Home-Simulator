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

    def toString(self):
        return "Sensor: " + self.getSensorName() + "\n\tState: " + str(self.getSensorState())


class Appliance(object):
    def __init__(self, applianceName, watts):
        self.applianceName = applianceName
        self.watts = watts
        self.sensor = Sensor

    def getApplianceName(self):
        return self.applianceName

    def getSensor(self):
        return self.sensor

    def getWatts(self):
        return self.watts

    def addSensor(self, sensor):
        self.sensor = sensor

    def toString(self):
        return "Appliance name: " + self.getApplianceName() + "\tWatts: " + str(self.getWatts())

class Room(object):
    def __init__(self, roomName):
        self.roomName = roomName
        self.appliances = []

    def getRoomName(self):
        return self.roomName

    def getAppliances(self):
        return self.appliances

    def getAppliance(self, appliance):
        for a in self.appliances:
            if a.getApplianceName() == appliance:
                return a

    def addAppliances(self, appliances):
        for appliance in appliances:
            self.appliances.append(appliance)

    def toString(self):
        roomDesc = "Room: " + self.getRoomName() + "\nAppliances: "
        for appliance in self.appliances:
            roomDesc += appliance.getApplianceName() + "\t"
        return roomDesc


class Home(object):
    def __init__(self):
        self.rooms = []

    def addRooms(self, rooms):
        for room in rooms:
            self.rooms.append(room)

    def getRoom(self, room):
        for r in self.rooms:
            if r.getRoomName() == room:
                return r

    def getRooms(self):
        return self.rooms


class Simulation(object):
    def __init__(self, env):
        self.env = env
        self.home = Home
        self.powerUsages = []
        self.waterUsages = []
        self.HvacUsages = []
        self.dailyUsages = []

    def createHome(self):
        self.home = Home()

        self.home.addRooms({Room("Master Bedroom"), Room("Kid 1 Bedroom"), Room("Kid 2 Bedroom"), Room("Master Bathroom"),
                 Room("Kids Bathroom"), Room("Garage"), Room("Living Room"), Room("Kitchen"),
                 Room("Laundry Room")})

        self.home.getRoom("Master Bedroom").addAppliances(
            {Appliance("Overhead Light", 60), Appliance("Lamp 1",  60), Appliance("Lamp 2",  60),
            Appliance("Bedroom TV", 636), Appliance("Window", 0), Appliance("Window", 0)})
        self.home.getRoom("Kid 1 Bedroom").addAppliances(
            {Appliance("Overhead Light", 60), Appliance("Lamp 1", 60), Appliance("Lamp 2", 60),
             Appliance("Window 1", 0), Appliance("Window 2", 0)})
        self.home.getRoom("Kid 2 Bedroom").addAppliances(
            {Appliance("Overhead Light", 60), Appliance("Lamp 1", 60), Appliance("Lamp 2", 60),
             Appliance("Window 1", 0), Appliance("Window 2", 0)})
        self.home.getRoom("Master Bathroom").addAppliances(
            {Appliance("Overhead Light", 60), Appliance("Bath Exhaust Fan", 30), Appliance("Bath", 0),
             Appliance("Shower", 0)})
        self.home.getRoom("Kids Bathroom").addAppliances(
            {Appliance("Overhead Light", 60), Appliance("Bath Exhaust Fan", 30), Appliance("Bath", 0),
             Appliance("Shower", 0)})
        self.home.getRoom("Garage").addAppliances(
            {Appliance("Door 1", 0), Appliance("Door 2", 0), Appliance("Window", 0),
             Appliance("Hot Water Heater", 4500)})
        self.home.getRoom("Living Room").addAppliances(
            {Appliance("Overhead Light", 60), Appliance("Lamp",  60), Appliance("Living Room TV", 636),
             Appliance("Door 1", 0), Appliance("Door 2", 0), Appliance("Window 1", 0),
             Appliance("Window 2", 0), Appliance("Hvac", 3500)})
        self.home.getRoom("Kitchen").addAppliances(
            {Appliance("Overhead Light", 60), Appliance("Stove", 3500), Appliance("Oven", 4000),
             Appliance("Microwave", 1100), Appliance("Refrigerator", 150), Appliance("Dishwasher", 1800),
             Appliance("Door", 0)})
        self.home.getRoom("Laundry Room").addAppliances({
            Appliance("Clothes Washer", 500), Appliance("Clothes Dryer", 3000)})

        for room in self.home.getRooms():
            for appliance in room.getAppliances():
                appliance.addSensor(Sensor(appliance.getApplianceName(), 0))

        return self.home

    def updatePowerUsage(self, sensor, startTime, endTime, usage, cost):
        self.powerUsages.append(PowerUsage(sensor, startTime, endTime, usage, cost))

    def updateWaterUsage(self, sensor, startTime, endTime, usage, cost):
        self.powerUsages.append(WaterUsage(sensor, startTime, endTime, usage, cost))

    def updateHvacUsage(self, sensor, startTime, endTime, temperature, usage, cost):
        self.powerUsages.append(HvacUsage(sensor, startTime, endTime, usage, cost))

    def updateDailyUsage(self,  date, totalWaterUsage, totalPowerUsage, totalHvacUsage, totalPowerCost, totalWaterCost, totalHvacCost):
        self.dailyUsages.append(DailyUsage( date, totalWaterUsage, totalPowerUsage, totalHvacUsage, totalPowerCost, totalWaterCost, totalHvacCost))


    def printHouseDetail(self):
        print("Home Detail: \n")

        print("Rooms: \n")
        for room in self.home.getRooms():
            print(room.getRoomName() + ": \n")
            for appliance in room.getAppliances():
                print(appliance.getSensor().toString())
            print()


    def calculatePowerCost(self, watts, time):
        return (watts * (time/3600)) * .12

    def calculatePowerUsage(self, watts, time):
        return watts * (time/3600)



def simulate():
    env = simpy.Environment()
    s = Simulation(env)

    home = s.createHome()

    s.printHouseDetail()

    print("\nSimulating power usage for appliances in rooms.\n")

    # SIMULATE SOMETHING

simulate()








