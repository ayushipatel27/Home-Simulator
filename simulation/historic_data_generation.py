import random, json, requests
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
        self.home = Home()
        self.rooms = []
        self.appliances = []
        self.sensors = []
        self.powerUsages = []
        self.waterUsages = []
        self.hvacUsages = []
        self.dailyUsages = []
        self.states = []

    def createHome(self):
        self.home = Home()

        self.home.addRooms({Room(1, "Master Bedroom"), Room(2, "Kid 1 Bedroom"), Room(3, "Kid 2 Bedroom"), Room(4, "Master Bathroom"),
                 Room(5, "Kids Bathroom"), Room(6, "Garage"), Room(7, "Living Room"), Room(8, "Kitchen"),
                 Room(9, "Laundry Room")})

        self.home.getRoom("Master Bedroom").addAppliances(
            {Appliance(1, "Overhead Light", 60), Appliance(2, "Lamp 1",  60), Appliance(3, "Lamp 2",  60),
            Appliance(4, "Bedroom TV", 636), Appliance(5, "Window", 0), Appliance(6, "Window", 0)})

        self.home.getRoom("Kid 1 Bedroom").addAppliances(
            {Appliance(7, "Overhead Light", 60), Appliance(8, "Lamp 1", 60), Appliance(9, "Lamp 2", 60),
             Appliance(10, "Window 1", 0), Appliance(11, "Window 2", 0)})

        self.home.getRoom("Kid 2 Bedroom").addAppliances(
            {Appliance(12, "Overhead Light", 60), Appliance(13, "Lamp 1", 60), Appliance(14, "Lamp 2", 60),
             Appliance(15, "Window 1", 0), Appliance(16, "Window 2", 0)})

        self.home.getRoom("Master Bathroom").addAppliances(
            {Appliance(17, "Overhead Light", 60), Appliance(18, "Bath Exhaust Fan", 30), Appliance(19, "Bath", 0),
             Appliance(20, "Shower", 0)})

        self.home.getRoom("Kids Bathroom").addAppliances(
            {Appliance(21, "Overhead Light", 60), Appliance(22, "Bath Exhaust Fan", 30), Appliance(23, "Bath", 0),
             Appliance(24, "Shower", 0)})

        self.home.getRoom("Garage").addAppliances(
            {Appliance(25, "Garage Door 1", 0), Appliance(26, "Garage Door 2", 0), Appliance(27, "Window 1", 0),
             Appliance(28, "HVAC", 3500)})


        self.home.getRoom("Living Room").addAppliances(
            {Appliance(29, "Overhead Light", 60), Appliance(30, "Lamp",  60), Appliance(31, "Living Room TV", 636),
             Appliance(32, "Back Door", 0), Appliance(33, "Front Door", 0), Appliance(34, "Window 1", 0),
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
            self.rooms.append({'roomname': room.getRoomName()})

    def addAppliances(self):
        for room in self.home.getRooms():
            for appliance in room.getAppliances():
                self.appliances.append({'sensorid': appliance.getSensor().getId(),
                                        'powerusage': appliance.getWatts(),
                                        'powerrate': appliance.getPowerRate(),
                                        'appliancename': appliance.getApplianceName()})

    def addSensors(self):
        for room in self.home.getRooms():
            for appliance in room.getAppliances():
                self.sensors.append({'sensorname': appliance.getSensor().getSensorName(),
                                     'sensorstate': appliance.getSensor().getSensorState(),
                                     'roomid': room.getId()})

    def addPowerUsage(self, sensorid, starttime, endtime, usage, cost):
        self.powerUsages.append({'timestamp': starttime,
                                 'sensorid': sensorid,
                                 'endtimestamp': endtime,
                                 'usage': usage,
                                 'cost': cost})


    def addWaterUsage(self, sensorid, starttime, endtime, usage, cost):
        self.waterUsages.append({'timestamp': starttime,
                                 'sensorid': sensorid,
                                 'endtimestamp': endtime,
                                 'usage': usage,
                                 'cost': cost})

    def addHvacUsage(self, sensorid, starttime, endtime, temperature, usage, cost):
        self.hvacUsages.append({'timestamp': starttime,
                                 'sensorid': sensorid,
                                 'endtimestamp': endtime,
                                 'usage': usage,
                                 'cost': cost,
                                 'temperature': temperature})

    def addDailyUsage(self,  date, totalwaterusage, totalpowerusage, totalhvacusage, totalpowercost, totalwatercost, totalhvaccost):
        self.dailyUsages.append({'date': date.strftime("%Y-%m-%d"),
                                 'totalwaterusage': int(totalwaterusage),
                                 'totalpowerusage': int(totalpowerusage),
                                 'totalpowercost': int(totalpowercost),
                                 'totalwatercost':  int(totalwatercost),
                                 'totalhvacusage': int(totalhvacusage),
                                 'totalhvaccost': int(totalhvaccost)})


    def generateJson(self):
        rooms_json = json.dumps(self.rooms, indent=4, sort_keys=True)
        appliances_json = json.dumps(self.appliances, indent=4, sort_keys=True)
        sensors_json = json.dumps(self.sensors, indent=4, sort_keys=True)
        power_usages_json = json.dumps(self.powerUsages, indent=4, sort_keys=True)
        water_usages_json = json.dumps(self.waterUsages, indent=4, sort_keys=True)
        hvac_usages_json = json.dumps(self.hvacUsages, indent=4, sort_keys=True)
        daily_usages_json = json.dumps(self.dailyUsages, indent=4, sort_keys=True)

        print("Rooms: " + rooms_json)
        print("Appliances: " + appliances_json)
        print("Sensors: " + sensors_json)
        print("Power Usages: " + power_usages_json)
        print("Water Usages: " + water_usages_json)
        print("HVAC Usages: " + hvac_usages_json)
        print("Daily Usages: " + daily_usages_json)

        requests.post('http://127.0.0.1:8000/api/insert/rooms/', rooms_json)
        requests.post('http://127.0.0.1:8000/api/insert/sensors/', sensors_json)
        requests.post('http://127.0.0.1:8000/api/insert/appliances/', appliances_json)
        requests.post('http://127.0.0.1:8000/api/insert/powerusage/', power_usages_json)
        requests.post('http://127.0.0.1:8000/api/insert/waterusage/', water_usages_json)
        requests.post('http://127.0.0.1:8000/api/insert/hvacusage/', hvac_usages_json)
        requests.post('http://127.0.0.1:8000/api/insert/dailyusage/', daily_usages_json)

    def monthlyReport(self):
        totalPowerCost = 0
        totalWaterCost = 0
        totalHvacCost = 0
        for i in self.dailyUsages:
            for j in i:
                if j == 'totalpowercost':
                    totalPowerCost += i['totalpowercost']
                if j == 'totalwatercost':
                    totalWaterCost += i['totalwatercost']
                if j == 'totalhvaccost':
                    totalHvacCost += i['totalhvaccost']
        return {'totalpowercost' : totalPowerCost, 'totalwatercost': totalWaterCost, 'totalhvaccost': totalHvacCost}


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
        return t.strftime("%H:%M:%S")

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
            if self.isWeekday(day):
                return 480
            else:
                return 960
        if "Window" in appliance.getApplianceName():
            if self.isWeekday(day):
                return random.randint(7200, 10800)
            else:
                return random.randint(14400, 18000)
        if appliance.getApplianceName() == "HVAC" :
            return random.randint(21600, 28800)
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

    def startRoutineUsage(self, timeOfDay, desiredTimeOn, appliance, singleDate):
        sensor = appliance.getSensor()

        totalTimeOn = 0

        startTime = singleDate.strftime('%Y-%m-%d ') + self.convertSecondsToTime(timeOfDay)
        sensor.setSensorState(1)

        endTime = singleDate.strftime('%Y-%m-%d ') + self.convertSecondsToTime(timeOfDay + desiredTimeOn)
        sensor.setSensorState(0)

        powerUsage = self.calculatePowerCost(appliance.getWatts(), desiredTimeOn)
        powerCost = self.calculatePowerUsage(appliance.getWatts(), desiredTimeOn)
        waterUsage = self.calculateWaterUsage(appliance)
        waterCost = self.calculateWaterCost(appliance)
        hvacUsage = 0
        hvacCost = 0

        totalTimeOn += desiredTimeOn

        if powerUsage != 0:
            self.addPowerUsage(sensor.getId(), startTime, endTime, powerUsage, powerCost)

        if waterUsage != 0:
            self.addWaterUsage(sensor.getId(), startTime, endTime, waterUsage, waterCost)

        return {'powerUsage' : powerUsage, 'powerCost': powerCost, 'waterUsage': waterUsage, 'waterCost': waterCost, 'hvacUsage': hvacUsage, 'hvacCost': hvacCost}


    def startRandomUsage(self, day, desiredTimeOn, appliance, singleDate):
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
        hvacUsage = 0
        hvacCost = 0

        if self.isWeekday(day):
            while wakeTime <= currentTime <= sleepTime:
                if totalTimeOn < desiredTimeOn:
                    timeOn = random.randint(1, desiredTimeOn)
                    randomTime = self.generateRandomTime(currentTime, wakeTime, sleepTime)

                    if (currentTime + timeOn) > leaveTime and currentTime < leaveTime:
                        timeOn = leaveTime - currentTime

                    currentTime += randomTime

                    startTime = singleDate.strftime('%Y-%m-%d ') + self.convertSecondsToTime(currentTime)
                    sensor.setSensorState(1)

                    currentTime += timeOn
                    totalTimeOn += timeOn

                    endTime = singleDate.strftime('%Y-%m-%d ') + self.convertSecondsToTime(currentTime)
                    sensor.setSensorState(0)

                    if leaveTime <= currentTime <= comeHomeTime:
                        currentTime += (comeHomeTime - leaveTime)

                    usage = self.calculatePowerUsage(appliance.getWatts(), totalTimeOn)
                    powerUsage += usage
                    cost = self.calculatePowerCost(appliance.getWatts(), totalTimeOn)
                    powerCost += cost

                    if appliance.getApplianceName() == "HVAC":
                        temperature = random.randint(60, 80)
                        hvacUsage += usage
                        hvacCost += cost

                        self.addHvacUsage(sensor.getId(), startTime, endTime, temperature, usage, cost)
                    else:
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

                        startTime = singleDate.strftime('%Y-%m-%d ') + self.convertSecondsToTime(currentTime)
                        sensor.setSensorState(1)

                        currentTime += timeOn
                        totalTimeOn += timeOn

                        endTime = singleDate.strftime('%Y-%m-%d ') + self.convertSecondsToTime(currentTime)
                        sensor.setSensorState(0)

                        usage = self.calculatePowerUsage(appliance.getWatts(), totalTimeOn)
                        powerUsage += usage
                        cost = self.calculatePowerCost(appliance.getWatts(), totalTimeOn)
                        powerCost += cost

                        if appliance.getApplianceName() == "HVAC":
                            temperature = random.randint(60, 80)
                            hvacUsage += usage
                            hvacCost += cost
                            self.addHvacUsage(sensor.getId(), startTime, endTime, temperature, usage, cost)
                        else:
                            self.addPowerUsage(sensor.getId(), startTime, endTime, usage, cost)

                    else:
                        break
                else:
                    break

        return {'powerUsage' : powerUsage, 'powerCost': powerCost, 'waterUsage': waterUsage, 'waterCost': waterCost, 'hvacUsage': hvacUsage, 'hvacCost': hvacCost}

    def simulateUsage(self, appliance, day, singleDate):

        desiredTimeOn = self.getDurationOn(appliance, day)

        cleaningDays = random.choice(["0", "1", "2", "3", "4", "5", "6"])

        if appliance.getApplianceName() == "HVAC":
            usages = self.startRandomUsage(day, desiredTimeOn, appliance, singleDate)
            return usages

        elif appliance.getApplianceName() == "Refrigerator":
            usages = self.startRoutineUsage(0, desiredTimeOn, appliance, singleDate)
            return usages

        elif appliance.getApplianceName() == "Clothes Dryer":
            if str(day) in cleaningDays:
                randomTime = random.randint(63000, 72000)
                usages = self.startRoutineUsage(randomTime, desiredTimeOn, appliance, singleDate)
                return usages

        elif appliance.getApplianceName() == "Clothes Washer":
            if str(day) in cleaningDays:
                randomTime = random.randint(63000, 72000)
                usages = self.startRoutineUsage(randomTime, desiredTimeOn, appliance, singleDate)
                return usages

        elif appliance.getApplianceName() == "Dishwasher":
            if str(day) in cleaningDays:
                randomTime = random.randint(63000, 72000)
                usages = self.startRoutineUsage(randomTime, desiredTimeOn, appliance, singleDate)
                return usages

        elif appliance.getApplianceName() == "Bath":
            randomTime = random.randint(64800, 72000)
            usages = self.startRoutineUsage(randomTime, desiredTimeOn, appliance, singleDate)
            return usages

        elif appliance.getApplianceName() == "Shower":
            randomTime = random.randint(18000, 21600)
            usages = self.startRoutineUsage(randomTime, desiredTimeOn, appliance, singleDate)
            return usages

        else:
            usages = self.startRandomUsage(day, desiredTimeOn, appliance, singleDate)
            return usages


    def simulate(self):
        home = self.createHome()

        self.addRooms()
        self.addAppliances()
        self.addSensors()

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
                for appliance in room.getAppliances():
                    if appliance.getApplianceName() == "HVAC":
                        usages = self.simulateUsage(appliance, day, singleDate)
                    if "Lamp" in appliance.getApplianceName():
                        usages = self.simulateUsage(appliance, day, singleDate)
                    if appliance.getApplianceName() == "Shower":
                        if self.isWeekday(day):
                            for i in range(2):
                                usages = self.simulateUsage(appliance, day, singleDate)
                        else:
                            for i in range(3):
                                usages = self.simulateUsage(appliance, day, singleDate)
                    if appliance.getApplianceName() == "Bath":
                        if self.isWeekday(day):
                            for i in range(2):
                                usages = self.simulateUsage(appliance, day, singleDate)
                        else:
                            for i in range(3):
                                usages = self.simulateUsage(appliance, day, singleDate)
                    else:
                        usages = self.simulateUsage(appliance, day, singleDate)

                    try:
                        totalHvacUsage += usages['hvacUsage']
                        totalHvacCost += usages['hvacCost']
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
