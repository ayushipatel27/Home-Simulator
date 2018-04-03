import random
import requests, json, ast
from darksky import forecast
import datetime, time
import threading as t

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

    def createHome(self):
        self.home = Home()

        self.home.addRooms({Room(1, "Master Bedroom"), Room(2, "Kid 1 Bedroom"), Room(3, "Kid 2 Bedroom"), Room(4, "Master Bathroom"),
                 Room(5, "Kids Bathroom"), Room(6, "Garage"), Room(7, "Living Room"), Room(8, "Kitchen"),
                 Room(9, "Laundry Room")})

        self.home.getRoom("Master Bedroom").addAppliances(
            [Appliance(1, "Overhead Light", 60), Appliance(2, "Lamp", 60), Appliance(3, "Lamp", 60),
             Appliance(4, "Bedroom TV", 636), Appliance(5, "Window", 0), Appliance(6, "Window", 0)])

        self.home.getRoom("Kid 1 Bedroom").addAppliances(
            [Appliance(7, "Overhead Light", 60), Appliance(8, "Lamp", 60), Appliance(9, "Lamp", 60),
             Appliance(10, "Window", 0), Appliance(11, "Window", 0)])

        self.home.getRoom("Kid 2 Bedroom").addAppliances(
            [Appliance(12, "Overhead Light", 60), Appliance(13, "Lamp", 60), Appliance(14, "Lamp", 60),
             Appliance(15, "Window", 0), Appliance(16, "Window", 0)])

        self.home.getRoom("Master Bathroom").addAppliances(
            [Appliance(17, "Overhead Light", 60), Appliance(18, "Bath Exhaust Fan", 30), Appliance(19, "Bath", 0),
             Appliance(20, "Shower", 0)])

        self.home.getRoom("Kids Bathroom").addAppliances(
            [Appliance(21, "Overhead Light", 60), Appliance(22, "Bath Exhaust Fan", 30), Appliance(23, "Bath", 0),
             Appliance(24, "Shower", 0)])

        self.home.getRoom("Garage").addAppliances(
            [Appliance(25, "Door", 0), Appliance(26, "Door", 0), Appliance(27, "Window", 0),
             Appliance(28, "Hot Water Heater", 4500)])

        self.home.getRoom("Living Room").addAppliances(
            [Appliance(29, "Overhead Light", 60), Appliance(30, "Lamp", 60), Appliance(31, "Living Room TV", 636),
             Appliance(32, "Door", 0), Appliance(33, "Front Door", 0), Appliance(34, "Window", 0),
             Appliance(35, "Window", 0), Appliance(36, "HVAC", 3500)])

        self.home.getRoom("Kitchen").addAppliances(
            [Appliance(37, "Overhead Light", 60), Appliance(38, "Stove", 3500), Appliance(39, "Oven", 4000),
             Appliance(40, "Microwave", 1100), Appliance(41, "Refrigerator", 150), Appliance(42, "Dishwasher", 1800),
             Appliance(43, "Door", 0)])

        self.home.getRoom("Laundry Room").addAppliances(
            [Appliance(44, "Clothes Washer", 500), Appliance(45, "Clothes Dryer", 3000)])

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

    def getProbability(self, appliance, day):
        r = random.random()
        if appliance.getApplianceName() == "Overhead Light":
            return r
        if appliance.getApplianceName() == "Lamp":
            return r
        if appliance.getApplianceName() == "Living Room TV":
            if self.isWeekday(day):
                return 0.1666
            else:
                return 0.3333
        if appliance.getApplianceName() == "Bedroom TV":
            if self.isWeekday(day):
                return 0.0833
            else:
                return 0.1666
        if appliance.getApplianceName() == "Bath Exhaust Fan":
            return r
        if appliance.getApplianceName() == "Stove":
            if self.isWeekday(day):
                return 0.0104
            else:
                return 0.0208
        if appliance.getApplianceName() == "Oven":
            if self.isWeekday(day):
                return 0.03125
            else:
                return 0.04166
        if appliance.getApplianceName() == "Microwave":
            if self.isWeekday(day):
                return 0.0138
            else:
                return 0.0208
        if appliance.getApplianceName() == "Refrigerator":
            return 0.9999
        if appliance.getApplianceName() == "Clothes Dryer":
            return 0.0119
        if appliance.getApplianceName() == "Clothes Washer":
            return 0.0119
        if appliance.getApplianceName() == "Dishwasher":
            return 0.0178
        if appliance.getApplianceName() == "Shower":
            if self.isWeekday(day):
                return 0.02083
            else:
                return 0.03125
        if appliance.getApplianceName() == "Bath":
            if self.isWeekday(day):
                return 0.0417
            else:
                return 0.0625
        if appliance.getApplianceName() == "Door":
            if self.isWeekday(day):
                return 0.0055
            else:
                return 0.0111
        if appliance.getApplianceName() == "Window":
            return r

    def calculatePowerCost(self, watts, time):
        return ((watts * (time/3600))/1000) * .12         # returns $ for kilowatts per hour

    def calculatePowerUsage(self, watts, time):
        return (watts * (time/3600))/1000                 #returns kilowatts per hour

    def calculateWaterCost(self, appliance):
        timeHotWaterUsed = self.getGallons(appliance) * self.getHotWaterPercentage(appliance) * 240
        return self.calculatePowerCost(4500, timeHotWaterUsed)

    def calculateWaterUsage(self, appliance):
        return self.getGallons(appliance)

    def convertToSeconds(self, time):
        year, month, day, hour, minute, second, weekday, yearday, daylight = time
        return (hour*3600) + (minute*60) + second

    def isWeekday(self, day):
        if day < 5:
            return True
        else:
            return False


    def getCurrentState(self):
        r = requests.get('http://127.0.0.1:8000/api/gethousestate/')
        state = r.json()
        return state

    def addPowerUsage(self, sensorids, starttime, endtime, usage, cost):
        return {'timestamp': starttime,
                 'sensorids': sensorids,
                 'endtimestamp': endtime,
                 'usage': usage,
                 'cost': cost}


    def addWaterUsage(self, sensorids, starttime, endtime, usage, cost):
        return {'timestamp': starttime,
                 'sensorids': sensorids,
                 'endtimestamp': endtime,
                 'usage': usage,
                 'cost': cost}

    def addHvacUsage(self, sensorid, starttime, endtime, temperature, usage, cost):
        return {'timestamp': starttime,
                'sensorid': sensorid,
                 'endtimestamp': endtime,
                 'usage': usage,
                 'cost': cost,
                 'temperature': temperature}

    def addWeather(self, timestamp, temperature, precipitation, chanceofprecipitation, state):
        return {'timestamp': timestamp,
                'temperature': temperature,
                'precipitation' : precipitation,
                'chanceofprecipitation': chanceofprecipitation,
                'state': state}

    def updateWeather(self, now):
        darkSkyKey = "ce3ee51d4f49051735382ee071219e87"
        bhamLatitude = 33.5207
        bhamLongitude = -86.8025
        birmingham = forecast(darkSkyKey, bhamLatitude, bhamLongitude)

        externalTemp = birmingham.temperature
        precipitationIntensity = birmingham.precipIntensity
        precipitationProbability = birmingham.precipProbability
        summary = birmingham.summary

        weather = self.addWeather(now, externalTemp, precipitationIntensity, precipitationProbability, summary)

        return weather

    def updatePowerUsage(self, appliances, home, state, now, day):
        appliancesOn = []
        r = random.random()

        powerUsage = 0
        powerCost = 0

        sensorids = state['home']['powerusage']['sensorids']
        ids = ast.literal_eval(sensorids)

        for room in home.getRooms():
            for appliance in room.getAppliances():
                for id in ids:
                    if appliance.getId() == id:
                        powerUsage += self.calculatePowerUsage(appliance.getWatts(), 600)
                        powerCost += self.calculatePowerCost(appliance.getWatts(), 600)

        for appliance in appliances:
            probability = self.getProbability(appliance, day)
            if r < probability:
                appliance.getSensor().setSensorState(1)
                appliancesOn.append(appliance.getSensor().getId())
            if r > probability:
                appliance.getSensor().setSensorState(0)

        appliancesOn = str(appliancesOn)

        return self.addPowerUsage(appliancesOn, '', now, powerUsage, powerCost)

    def updateWaterUsage(self, appliances, home, state, now, day):
        appliancesOn = []
        r = random.random()

        waterUsage = 0
        waterCost = 0

        sensorids = state['home']['waterusage']['sensorids']
        ids = ast.literal_eval(sensorids)

        for room in home.getRooms():
            for appliance in room.getAppliances():
                for id in ids:
                    if appliance.getId() == id:
                        waterUsage += self.calculateWaterUsage(appliance)
                        waterCost += self.calculateWaterCost(appliance)

        for appliance in appliances:
            probability = self.getProbability(appliance, day)
            if r < probability:
                appliance.getSensor().setSensorState(1)
                appliancesOn.append(appliance.getSensor().getId())
            if r > probability:
                appliance.getSensor().setSensorState(0)

        appliancesOn = str(appliancesOn)

        return self.addWaterUsage(appliancesOn, '', now, waterUsage, waterCost)

    def updateHvacUsage(self, appliances, internalTemp, externalTemp, now, day):
        applianceOn = []
        currentHouseState = 0
        lowestTemp = 68
        highestTemp = 75
        r = random.random()

        for appliance in appliances:
            if appliance == "Door":
                if self.isWeekday(day):
                    probability = 0.0055
                else:
                    probability = 0.0111
                if r < probability:
                    currentHouseState = 1
                else:
                    currentHouseState = 0
            else:
                probability = r
                if r < probability:
                    currentHouseState = 2
                else:
                    currentHouseState = 0

        if (currentHouseState == 0):
            internalTemp = internalTemp + 0.033 * (externalTemp - internalTemp)
        elif (currentHouseState == 1):
            internalTemp = internalTemp + 0.4 * (externalTemp - internalTemp)
        elif (currentHouseState == 2):
            internalTemp = internalTemp + 0.2 * (externalTemp - internalTemp)

        deltaHigh = internalTemp - highestTemp
        deltaLow = lowestTemp - internalTemp

        if (deltaHigh > 0):
            hvacUsage = 0.0583 + (0.0583 * deltaHigh)
            hvacCost = hvacUsage * 0.12
            internalTemp = internalTemp - 1 + deltaHigh
            time = 60 + (60 * deltaHigh)
            deltaTime = datetime.timedelta(seconds=(-time))
        elif (deltaLow > 0):
            hvacUsage = 0.0583 + (0.0583 * deltaLow)
            hvacCost = hvacUsage * 0.12
            internalTemp = internalTemp + 1 + deltaLow
            time = 60 + (60 * deltaLow)
            deltaTime = datetime.timedelta(seconds=(-time))
        else:
            hvacUsage = 0
            hvacCost = 0
            deltaTime =datetime.timedelta(seconds=(0))

        applianceOn = str(applianceOn)

        startTime = datetime.datetime.now() + deltaTime

        return self.addHvacUsage(applianceOn, startTime.strftime('%Y-%m-%d %H:%M:%S'), now, internalTemp, hvacUsage, hvacCost)


    def simulateUsage(self, home):
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        day = datetime.date.today().weekday()

        power = []
        water = []
        hvac = []

        powerAppliances = ['Clothes Dryer', 'Clothes Washer', 'Dishwasher', 'Bath', 'Shower',
                           'Bedroom TV', 'Living Room TV', 'Oven', 'Stove', 'Microwave',
                           'Refrigerator', 'Bath Exhaust Fan', 'Lamp', 'Overhead Light']
        waterAppliances = ['Clothes Dryer', 'Clothes Washer', 'Dishwasher', 'Bath', 'Shower']
        hvacAppliances =['Door', 'Window']

        state = self.getCurrentState()

        print(state)

        for room in home.getRooms():
            for appliance in room.getAppliances():
                if appliance.getApplianceName() in powerAppliances:
                    power.append(appliance)
                if appliance.getApplianceName() in waterAppliances:
                    water.append(appliance)
                if appliance.getApplianceName() in hvacAppliances:
                    hvac.append(appliance)
                else:
                    pass

        currrentWeatherState = self.updateWeather(now)

        internalTemp = state['home']['hvacusage']['temperature']
        externalTemp = currrentWeatherState['temperature']

        currentPowerState = self.updatePowerUsage(power, home, state, now, day)
        currentWaterState = self.updateWaterUsage(water, home, state, now, day)
        currentHvacState = self.updateHvacUsage(hvac, internalTemp, externalTemp, now, day)

        state['home']['powerusage'] = currentPowerState
        state['home']['waterusage'] = currentWaterState
        state['home']['hvacusage'] = currentHvacState
        state['home']['weather'] = currrentWeatherState


        print(state)

        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        url = 'http://127.0.0.1:8000/api/update/housestate/'
        r = requests.post(url, data=json.dumps(state), headers=headers)

    def simulate(self):
        home = self.createHome()
        while True:
            t.Timer(600, self.simulateUsage(home))






# calling simulation to simulate usage.
s = Simulation()
s.simulate()
