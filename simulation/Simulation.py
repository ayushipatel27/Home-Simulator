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
    def __init__(self, id, sensorName, sensorState):
        self.id = id
        self.sensorName = sensorName
        self.sensorState = sensorState

    def getId(self):
        return self.id

    def getSensorName(self):
        return self.sensorName

    def getSensorState(self):
        return self.sensorState

    def setSensorState(self, sensorState):
        self.sensorState = sensorState

    def toString(self):
        return "Sensor: " + self.getSensorName() + "\n\tState: " + str(self.getSensorState())


class Appliance(object):
    def __init__(self, id, applianceName, watts):
        self.id = id
        self.applianceName = applianceName
        self.watts = watts
        self.powerRate = 0.12
        self.sensor = Sensor

    def getId(self):
        return self.id

    def getApplianceName(self):
        return self.applianceName

    def getSensor(self):
        return self.sensor

    def getWatts(self):
        return self.watts

    def getPowerRate(self):
        return self.powerRate

    def addSensor(self, sensor):
        self.sensor = sensor

    def toString(self):
        return "Appliance Id: " + str(self.getId()) \
               + "\n\tAppliance name: " + self.getApplianceName() \
               + "\n\tWatts: " + str(self.getWatts()) \
               + "\n\tSensor State: " + str(self.sensor.getSensorState()) + "\n"

class Room(object):
    def __init__(self, id, roomName):
        self.id = id
        self.roomName = roomName
        self.appliances = []

    def getId(self):
        return self.id

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

    def getRooms(self):
        return self.rooms

    def getRoom(self, room):
        for r in self.rooms:
            if r.getRoomName() == room:
                return r


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

        self.home.addRooms({Room(1, "Master Bedroom"), Room(2, "Kid 1 Bedroom"), Room(3, "Kid 2 Bedroom"), Room(4, "Master Bathroom"),
                 Room(5, "Kids Bathroom"), Room(6, "Garage"), Room(7, "Living Room"), Room(8, "Kitchen"),
                 Room(9, "Laundry Room")})

        self.home.getRoom("Master Bedroom").addAppliances(
            {Appliance(1, "Overhead Light", 60), Appliance(2, "Lamp 1",  60), Appliance(3, "Lamp 2",  60),
            Appliance(4, "Bedroom TV", 636), Appliance(5, "Window", 0), Appliance(6, "Window", 0)})

        self.home.getRoom("Kid 1 Bedroom").addAppliances(
            {Appliance(7, "Overhead Light", 60), Appliance(8, "Lamp 1", 60), Appliance(10, "Lamp 2", 60),
             Appliance(11, "Window 1", 0), Appliance(12, "Window 2", 0)})

        self.home.getRoom("Kid 2 Bedroom").addAppliances(
            {Appliance(13, "Overhead Light", 60), Appliance(14, "Lamp 1", 60), Appliance(15, "Lamp 2", 60),
             Appliance(16, "Window 1", 0), Appliance(17, "Window 2", 0)})

        self.home.getRoom("Master Bathroom").addAppliances(
            {Appliance(18, "Overhead Light", 60), Appliance(19, "Bath Exhaust Fan", 30), Appliance(20, "Bath", 0),
             Appliance(21, "Shower", 0)})

        self.home.getRoom("Kids Bathroom").addAppliances(
            {Appliance(22, "Overhead Light", 60), Appliance(23, "Bath Exhaust Fan", 30), Appliance(24, "Bath", 0),
             Appliance(25, "Shower", 0)})

        self.home.getRoom("Garage").addAppliances(
            {Appliance(26, "Garage Door 1", 0), Appliance(27, "Garage Door 2", 0), Appliance(28, "Window", 0),
             Appliance(29, "Hot Water Heater", 4500)})

        self.home.getRoom("Living Room").addAppliances(
            {Appliance(30, "Overhead Light", 60), Appliance(31, "Lamp",  60), Appliance(32, "Living Room TV", 636),
             Appliance(33, "Back Door", 0), Appliance(34, "Front Door", 0), Appliance(35, "Window 1", 0),
             Appliance(36, "Window 2", 0), Appliance(37, "Hvac", 3500)})

        self.home.getRoom("Kitchen").addAppliances(
            {Appliance(38, "Overhead Light", 60), Appliance(39, "Stove", 3500), Appliance(40, "Oven", 4000),
             Appliance(41, "Microwave", 1100), Appliance(42, "Refrigerator", 150), Appliance(43, "Dishwasher", 1800),
             Appliance(44, "Garage Door Into Home", 0)})

        self.home.getRoom("Laundry Room").addAppliances({
            Appliance(45, "Clothes Washer", 500), Appliance(46, "Clothes Dryer", 3000)})

        for room in self.home.getRooms():
            for appliance in room.getAppliances():
                appliance.addSensor(Sensor(appliance.getId(), appliance.getApplianceName(), 0))

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
                print(appliance.toString())
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








