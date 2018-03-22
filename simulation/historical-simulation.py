import random, json
from datetime import timedelta, time, date

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
        self.rooms = []
        self.appliances = []
        self.sensors = []
        self.powerUsages = []
        self.waterUsages = []
        self.hvacUsages = []
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
            {Appliance(26, "Garage Door 1", 0), Appliance(27, "Garage Door 2", 0), Appliance(28, "Window", 0)})

        self.home.getRoom("Living Room").addAppliances(
            {Appliance(29, "Overhead Light", 60), Appliance(30, "Lamp",  60), Appliance(31, "Living Room TV", 636),
             Appliance(32, "Back Door", 0), Appliance(32, "Front Door", 0), Appliance(34, "Window 1", 0),
             Appliance(35, "Window 2", 0), Appliance(36, "Hvac", 3500)})

        self.home.getRoom("Kitchen").addAppliances(
            {Appliance(37, "Overhead Light", 60), Appliance(38, "Stove", 3500), Appliance(39, "Oven", 4000),
             Appliance(40, "Microwave", 1100), Appliance(41, "Refrigerator", 150), Appliance(42, "Dishwasher", 1800),
             Appliance(43, "Garage Door Into Home", 0)})

        self.home.getRoom("Laundry Room").addAppliances({
            Appliance(44, "Clothes Washer", 500), Appliance(45, "Clothes Dryer", 3000)})

        for room in self.home.getRooms():
            for appliance in room.getAppliances():
                appliance.addSensor(Sensor(appliance.getId(), appliance.getApplianceName(), 0))

        return self.home

    def printHouseDetail(self):
        print("Home Detail: \n")

        print("Rooms: \n")
        for room in self.home.getRooms():
            print(room.getRoomName() + ": \n")
            for appliance in room.getAppliances():
                print(appliance.toString())
            print()

    def addRooms(self):
        for room in self.home.getRooms():
            self.rooms.append({'roomId': room.getId(), 'roomName': room.getRoomName()})

    def addAppliances(self):
        for room in self.home.getRooms():
            for appliance in room.getAppliances():
                self.appliances.append({'applianceId': appliance.getId(),
                                        'sensorId': appliance.getSensor().getId(),
                                        'powerUsage': appliance.getWatts(),
                                        'powerRate': appliance.getPowerRate(),
                                        'applianceName': appliance.getApplianceName()})

    def addSensors(self):
        for room in self.home.getRooms():
            for appliance in room.getAppliances():
                self.sensors.append({'sensorId': appliance.getSensor().getId(),
                                     'sensorName': appliance.getSensor().getSensorName(),
                                     'sensorState': appliance.getSensor().getSensorState(),
                                     'roomId': room.getId()})

    def addPowerUsage(self, sensorId, startTime, endTime, usage, cost):
        self.powerUsages.append({'timeStamp': startTime,
                                 'sensorId': sensorId,
                                 'endTimeStamp': endTime,
                                 'usage': usage,
                                 'cost': cost})

    def addWaterUsage(self, sensorId, startTime, endTime, usage, cost):
        self.waterUsages.append({'timeStamp': startTime,
                                 'sensorId': sensorId,
                                 'endTimeStamp': endTime,
                                 'usage': usage,
                                 'cost': cost})

    def addHvacUsage(self, sensorId, startTime, endTime, temperature, usage, cost):
        self.hvacUsages.append({'timeStamp': startTime,
                                 'sensorId': sensorId,
                                 'endTimeStamp': endTime,
                                 'usage': usage,
                                 'cost': cost})

    def addDailyUsage(self,  date, totalWaterUsage, totalPowerUsage, totalHvacUsage, totalPowerCost, totalWaterCost, totalHvacCost):
        self.dailyUsages.append({'date': date.strftime("%A, %B  %d, %Y"),
                                 'totalWaterUsage': int(totalWaterUsage),
                                 'totalPowerUsage': int(totalPowerUsage),
                                 'totalPowerCost': int(totalPowerCost),
                                 'totalWaterCost':  int(totalWaterCost),
                                 'totalHvacUsage': int(totalHvacUsage),
                                 'totalHvacCost': int(totalHvacCost)})
    def monthlyReport(self):
        totalPowerCost = 0
        totalWaterCost = 0
        for i in self.dailyUsages:
            for j in i:
                if j == 'totalPowerCost':
                    totalPowerCost += i['totalPowerCost']
                if j == 'totalWaterCost':
                    totalWaterCost += i['totalWaterCost']
        return {'totalPowerCost' : totalPowerCost, 'totalWaterCost': totalWaterCost}

    def generateJson(self):
        self.addRooms()
        self.addAppliances()
        self.addSensors()

        rooms_json = json.dumps(self.rooms, indent=4, sort_keys=True)
        appliances_json = json.dumps(self.appliances, indent=4, sort_keys=True)
        sensors_json = json.dumps(self.sensors,indent=4, sort_keys=True)
        power_usages_json = json.dumps(self.powerUsages, indent=4, sort_keys=True)
        water_usages_json = json.dumps(self.waterUsages, indent=4, sort_keys=True)
        daily_usages_json = json.dumps(self.dailyUsages, indent=4, sort_keys=True)

        print(rooms_json)
        print(appliances_json)
        print(sensors_json)
        print(power_usages_json)
        print(water_usages_json)
        print(daily_usages_json)

    def dateRange(self, startDate, endDate):
        for n in range(int((endDate - startDate).days)):
            yield startDate + timedelta(n)

    def convertSecondsToTime(self, seconds):
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        if h > 23:
            h = 23
            m = 59
            s = 59
        t = time(h,m,s)
        return t.strftime("%I:%M:%S %p")

    def isWeekday(self, day):
        if day < 5:
            return True
        else:
            return False

    def generateRandomTime(self, currentTime, startTime, endTime):
        randomTime = 0
        while startTime <= currentTime <= endTime:
            randomTime = random.randint(currentTime, currentTime+1800)
            if currentTime < randomTime:
                break
        return randomTime - currentTime

    def getDurationOn(self, appliance, day):
        if appliance.getApplianceName() == "Overhead Light":
            if self.isWeekday(day):
                return random.randint(10800, 25200)
            else:
                return random.randint(18000, 25200)
        if "Lamp" in appliance.getApplianceName():
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
            return 86400
        if appliance.getApplianceName() == "Clothes Dryer":
            return 1800
        if appliance.getApplianceName() == "Clothes Washer":
            return 1800
        if appliance.getApplianceName() == "Dishwasher":
            return 2700
        if appliance.getApplianceName() == "Shower":
            return random.randint(900, 1800)
        if appliance.getApplianceName() == "Bath":
            return random.randint(1800, 2700)
        if "Door" in appliance.getApplianceName():
            return 30
        else:
            return  0

    def getGallons(self, appliance):
        if appliance.getApplianceName() == "Bath":
            return 30
        if appliance.getApplianceName() == "Shower":
            return 25
        if appliance.getApplianceName() == "Dishwasher":
            return 6
        if appliance.getApplianceName() == "Clothes Washer":
            return 20
        else:
            return 0

    def getHotWaterPercentage(self, appliance):
        if appliance.getApplianceName() == "Bath":
            return 0.65
        if appliance.getApplianceName() == "Shower":
            return 0.65
        if appliance.getApplianceName() == "Dishwasher":
            return 1.00
        if appliance.getApplianceName() == "Clothes Washer":
            return 0.85
        else:
            return 0

    def calculatePowerCost(self, watts, time):
        return ((watts * (time/3600))/1000) * .12         # returns $ for kilowatts per hour

    def calculatePowerUsage(self, watts, time):
        return (watts * (time/3600))/1000                 #returns kilowatts per hour

    def calculateWaterCost(self, appliance):
        timeHotWaterUsed = self.getGallons(appliance) * self.getHotWaterPercentage(appliance) * 240
        return self.calculatePowerCost(4500, timeHotWaterUsed)

    def calculateWaterUsage(self, appliance):
        return self.getGallons(appliance)

    def startRoutineUsage(self, timeOfDay, desiredTimeOn, appliance):
        sensor = appliance.getSensor()

        totalTimeOn = 0

        startTime = self.convertSecondsToTime(timeOfDay)
        sensor.setSensorState(1)
        print("Turning on sensor at " + startTime)

        endTime = self.convertSecondsToTime(timeOfDay + desiredTimeOn)
        sensor.setSensorState(0)
        print("Turning off sensor at " + endTime)

        powerUsage = self.calculatePowerCost(appliance.getWatts(), desiredTimeOn)
        powerCost = self.calculatePowerUsage(appliance.getWatts(), desiredTimeOn)
        waterUsage = self.calculateWaterUsage(appliance)
        waterCost = self.calculateWaterCost(appliance)

        totalTimeOn += desiredTimeOn
        print("\nTotal time on should be " + str(desiredTimeOn) + " but is " + str(totalTimeOn))

        if powerUsage != 0:
            self.addPowerUsage(sensor.getId(), startTime, endTime, powerUsage, powerCost)
            print("Power Usage: %.2f kWh" % (powerUsage))
            print("Power Cost: $%.2f" % (powerCost))

        if waterUsage != 0:
            self.addWaterUsage(sensor.getId(), startTime, endTime, waterUsage, waterCost)
            print("Water Usage: %.2f kWh" % (waterUsage))
            print("Water Cost: $%.2f" % (waterCost))

        return {'powerUsage' : powerUsage, 'powerCost': powerCost, 'waterUsage': waterUsage, 'waterCost': waterCost}


    def startRandomUsage(self, day, desiredTimeOn, appliance):
        sensor = appliance.getSensor()

        wakeTime = 18000            #5:00 AM
        leaveTime = 27000           #7:30 AM
        comeHomeTime = 57600        #4:00 PM
        sleepTime = 73800           #10:30 PM
        currentTime = wakeTime

        totalTimeOn = 0
        powerUsage = 0
        powerCost = 0
        waterUsage = 0
        waterCost = 0

        if self.isWeekday(day):
            while wakeTime <= currentTime <= sleepTime:
                if totalTimeOn < desiredTimeOn:
                    timeOn = random.randint(1, desiredTimeOn)
                    randomTime = self.generateRandomTime(currentTime, wakeTime, sleepTime)

                    if (currentTime + timeOn) > leaveTime and currentTime < leaveTime:
                        timeOn = leaveTime - currentTime

                    currentTime += randomTime

                    startTime = self.convertSecondsToTime(currentTime)
                    appliance.getSensor().setSensorState(1)
                    print("Turning on sensor at " + startTime)

                    currentTime += timeOn
                    totalTimeOn += timeOn

                    endTime = self.convertSecondsToTime(currentTime)
                    appliance.getSensor().setSensorState(0)
                    print("Turning off sensor at " + endTime)

                    if leaveTime <= currentTime <= comeHomeTime:
                        currentTime += (comeHomeTime - leaveTime)

                    usage = self.calculatePowerUsage(appliance.getWatts(), totalTimeOn)
                    powerUsage += usage
                    cost = self.calculatePowerCost(appliance.getWatts(), totalTimeOn)
                    powerCost += cost

                    self.addPowerUsage(sensor.getId(), startTime, endTime, usage, cost)

                else:
                    break

        else:
            while wakeTime <= currentTime <= sleepTime:
                if totalTimeOn < desiredTimeOn:
                    timeOn = random.randint(1, desiredTimeOn)
                    randomTime = self.generateRandomTime(currentTime, wakeTime, sleepTime)
                    if currentTime + randomTime + timeOn < sleepTime:

                        currentTime += randomTime

                        startTime = self.convertSecondsToTime(currentTime)
                        appliance.getSensor().setSensorState(1)
                        print("Turning on sensor at " + startTime)

                        currentTime += timeOn
                        totalTimeOn += timeOn

                        endTime = self.convertSecondsToTime(currentTime)
                        appliance.getSensor().setSensorState(0)
                        print("Turning off sensor at " + endTime)

                        usage = self.calculatePowerUsage(appliance.getWatts(), totalTimeOn)
                        powerUsage += usage
                        cost = self.calculatePowerCost(appliance.getWatts(), totalTimeOn)
                        powerCost += cost

                        self.addPowerUsage(sensor.getId(), startTime, endTime, usage, cost)

                    else:
                        break
                else:
                    break

        print("\nTotal time on should be " + str(desiredTimeOn) + " but is " + str(totalTimeOn))
        print("Power Usage: %.2f kWh" % (powerUsage))
        print("Power Cost: $%.2f" % (powerCost))

        return {'powerUsage' : powerUsage, 'powerCost': powerCost, 'waterUsage': waterUsage, 'waterCost': waterCost}

    def simulateUsage(self, appliance, day):

        desiredTimeOn = self.getDurationOn(appliance, day)

        cleaningDays = random.choice(["0", "1", "2", "3", "4", "5", "6"])

        if "Door" in appliance.getApplianceName():
            return {'powerUsage' : 0, 'powerCost': 0, 'waterUsage': 0, 'waterCost': 0}

        if "Window" in appliance.getApplianceName():
            return {'powerUsage' : 0, 'powerCost': 0, 'waterUsage': 0, 'waterCost': 0}

        elif appliance.getApplianceName() == "Refrigerator":
            usages = self.startRoutineUsage(0, desiredTimeOn, appliance)
            return usages

        elif appliance.getApplianceName() == "Clothes Dryer":
            if str(day) in cleaningDays:
                randomTime = random.randint(63000, 72000)
                usages = self.startRoutineUsage(randomTime, desiredTimeOn, appliance)
                return usages

        elif appliance.getApplianceName() == "Clothes Washer":
            if str(day) in cleaningDays:
                randomTime = random.randint(63000, 72000)
                usages = self.startRoutineUsage(randomTime, desiredTimeOn, appliance)
                return usages

        elif appliance.getApplianceName() == "Dishwasher":
            if str(day) in cleaningDays:
                randomTime = random.randint(63000, 72000)
                usages = self.startRoutineUsage(randomTime, desiredTimeOn, appliance)
                return usages

        elif appliance.getApplianceName() == "Bath":
            randomTime = random.randint(64800, 72000)
            usages = self.startRoutineUsage(randomTime, desiredTimeOn, appliance)
            return usages

        elif appliance.getApplianceName() == "Shower":
            randomTime = random.randint(18000, 21600)
            usages = self.startRoutineUsage(randomTime, desiredTimeOn, appliance)
            return usages

        else:
            usages = self.startRandomUsage(day, desiredTimeOn, appliance)
            return usages


    def simulate(self):
        home = self.createHome()

        startDate = date(2018, 2, 1)
        endDate = date(2018, 3, 1)

        for singleDate in self.dateRange(startDate, endDate):
            day = singleDate.weekday()

            totalPowerUsage = 0
            totalPowerCost = 0
            totalWaterUsage = 0
            totalWaterCost = 0
            totalHvacUsage = 0
            totalHvacCost = 0

            for room in home.getRooms():
                print("Room: " + room.getRoomName() + "\n")

                for appliance in room.getAppliances():

                    print("Toggling sensor states for appliance " + appliance.getApplianceName() + ": \n")

                    if "Door" in appliance.getApplianceName():
                        usages = self.simulateUsage(appliance, day)
                    if "Window" in appliance.getApplianceName():
                        usages = self.simulateUsage(appliance, day)
                    if "Lamp" in appliance.getApplianceName():
                        usages = self.simulateUsage(appliance, day)
                    if appliance.getApplianceName() == "Shower":
                        if self.isWeekday(day):
                            for i in range(2):
                                usages = self.simulateUsage(appliance, day)
                        else:
                            for i in range(3):
                                usages = self.simulateUsage(appliance, day)
                    if appliance.getApplianceName() == "Bath":
                        if self.isWeekday(day):
                            for i in range(2):
                                usages = self.simulateUsage(appliance, day)
                        else:
                            for i in range(3):
                                usages = self.simulateUsage(appliance, day)
                    else:
                        usages = self.simulateUsage(appliance, day)

                    try:
                        totalPowerUsage += usages['powerUsage']
                        totalPowerCost += usages['powerCost']
                        totalWaterUsage += usages['waterUsage']
                        totalWaterCost += usages['waterCost']
                    except Exception:
                        pass
                        # gives error NoneType for one of these without exception. \_o_/

            self.addDailyUsage(singleDate, totalWaterUsage, totalPowerUsage, totalHvacUsage, totalPowerCost, totalWaterCost, totalHvacCost)


        self.generateJson()

        print(self.monthlyReport())

# calling simulation to simulate usage.
s = Simulation()
s.simulate()