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
    def __init__(self):
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

    def convertSecondsToTime(self, seconds):
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        if h > 23:
            h = 23
        t = time(h,m,s)
        return t.strftime("%I:%M:%S %p")

    def isWeekday(self, day):
        days = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]
        if day in days[0:5]:
            return True
        elif day in days[5:7]:
            return False

    def generateRandomTime(self, currentTime, startTime, endTime):
        randomTime = 0
        while startTime <= currentTime <= endTime:
            randomTime = random.randint(currentTime, currentTime+1800)
            if currentTime < randomTime:
                break
        return randomTime - currentTime

    def getTimeOn(self, appliance, day):
        if appliance.getApplianceName() == "Overhead Light":
            if self.isWeekday(day):
                return random.randint(10800, 25200)
            else:
                return random.randint(18000, 25200)
        if appliance.getApplianceName() == "Lamp":
            if self.isWeekday(day):
                return random.randint(3600, 7200)
            else:
                return random.randint(3600, 7200)
        if appliance.getApplianceName() == "Living Room TV":
            if self.isWeekday(day):
                return 14400
            else:
                return 28800
        if appliance.getApplianceName() == "Bedroom TV":
            if self.isWeekday(day):
                return 7200
            else:
                return 4400
        if appliance.getApplianceName() == "Bath Exhaust Fan":
            if self.isWeekday(day):
                return random.randint(7200, 14400)
            else:
                return random.randint(7200, 14400)
        if appliance.getApplianceName() == "Stove":
            if self.isWeekday(day):
                return 900
            else:
                return 1800
        if appliance.getApplianceName() == "Oven":
            if self.isWeekday(day):
                return 2700
            else:
                return 3600
        if appliance.getApplianceName() == "Microwave":
            if self.isWeekday(day):
                return 1200
            else:
                return 1800
        if appliance.getApplianceName() == "Refrigerator":
            if self.isWeekday(day):
                return 86400


    def simulatePowerUsage(self, appliance, day):
        print("\n" + "Toggling sensors for appliance " + appliance.getApplianceName())

        wakeTime = 18000            #5:00 AM
        leaveTime = 27000           #7:30 AM
        comeHomeTime = 57600        #4:00 PM
        sleepTime = 73800           #10:30 PM
        currentTime = wakeTime
        desiredTimeOn = self.getTimeOn(appliance, day)
        totalTimeOn = 0
        totalUsage = 0
        totalCost = 0

        # Todo: The sensors turns on after leave time sometimes
        # Todo: Try to add something where the sensor does not turn off after leave time

        if self.isWeekday(day):
            while wakeTime <= currentTime <= sleepTime:
                if totalTimeOn < desiredTimeOn:
                    timeOn = random.randint(1, desiredTimeOn)
                    timeOff = random.randint(1, desiredTimeOn)
                    randomTime = self.generateRandomTime(currentTime, wakeTime, sleepTime)

                    if currentTime + randomTime + timeOn + timeOff < sleepTime:
                        currentTime += randomTime + timeOn
                        totalTimeOn += timeOn

                        appliance.getSensor().setSensorState(1)
                        print("Turning on sensor at " + str(self.convertSecondsToTime(currentTime)))

                        currentTime += timeOff

                        appliance.getSensor().setSensorState(0)
                        print("Turning off sensor at " + str(self.convertSecondsToTime(currentTime)))

                        usage = self.calculatePowerUsage(appliance.getWatts(), totalTimeOn)
                        totalUsage += usage
                        cost = self.calculatePowerCost(appliance.getWatts(), totalTimeOn)
                        totalCost += cost

                    else:
                        break

                    if leaveTime < currentTime < comeHomeTime:
                        currentTime += (comeHomeTime - leaveTime)
                else:
                    break

        else:
            while wakeTime <= currentTime <= sleepTime:
                if totalTimeOn < desiredTimeOn:
                    timeOn = random.randint(1, desiredTimeOn)
                    timeOff = random.randint(1, desiredTimeOn)
                    randomTime = self.generateRandomTime(currentTime, wakeTime, sleepTime)
                    if currentTime + randomTime + timeOn + timeOff < sleepTime:

                        currentTime += randomTime + timeOn
                        totalTimeOn += timeOn

                        appliance.getSensor().setSensorState(1)
                        print("Turning on sensor at " + str(self.convertSecondsToTime(currentTime)))

                        currentTime += timeOff
                        appliance.getSensor().setSensorState(0)
                        print("Turning off sensor at " + str(self.convertSecondsToTime(currentTime)))

                        usage = self.calculatePowerUsage(appliance.getWatts(), totalTimeOn)
                        totalUsage += usage
                        cost = self.calculatePowerCost(appliance.getWatts(), totalTimeOn)
                        totalCost += cost
                    else:
                        break
                else:
                    break

        print("\nTotal time on should be " + str(timedelta(seconds=desiredTimeOn)) + " but is " + str(timedelta(seconds=totalTimeOn)))
        print("Total Usage: %.2f watts" % (totalUsage))
        print("Total Cost: $%.2f" % (totalCost))



def simulate():
    s = Simulation()

    home = s.createHome()

    s.printHouseDetail()

    day = "Mon"

    print("\nSimulating power usage for appliances in rooms.\n")


    for room in home.getRooms():
        print("\nRoom: " + room.getRoomName())
        for appliance in room.getAppliances():
            if appliance.getApplianceName() == "Overhead Light":
                s.simulatePowerUsage(appliance, day)
            if appliance.getApplianceName() == "Lamp":
                s.simulatePowerUsage(appliance, day)
            if appliance.getApplianceName() == "Living Room TV":
                s.simulatePowerUsage(appliance, day)
            if appliance.getApplianceName() == "Bedroom TV":
                s.simulatePowerUsage(appliance, day)
            if appliance.getApplianceName() == "Bath Exhaust Fan":
                s.simulatePowerUsage(appliance, day)
            if appliance.getApplianceName() == "Stove":
                s.simulatePowerUsage(appliance, day)
            if appliance.getApplianceName() == "Oven":
                s.simulatePowerUsage(appliance, day)
            if appliance.getApplianceName() == "Microwave":
                s.simulatePowerUsage(appliance, day)
            if appliance.getApplianceName() == "Refrigerator":
                usage = s.calculatePowerCost(appliance.getWatts(), 86400)
                cost = s.calculatePowerCost(appliance.getWatts(), 86400)


simulate()









