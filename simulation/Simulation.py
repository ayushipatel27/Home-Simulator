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
        return ((watts * (time/3600))/1000) * .12         # returns $ for kilowatts per hour

    def calculatePowerUsage(self, watts, time):
        return (watts * (time/3600))/1000                 #returns kilowatts per hour

    def calculateWaterCost(self, appliance):
        timeHotWaterUsed = self.getGallons(appliance) * self.getHotWaterPercentage(appliance) * 240
        return self.calculatePowerCost(4500, timeHotWaterUsed)

    def calculateWaterUsage(self, appliance):
        return self.getGallons(appliance)

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
            if self.isWeekday(day):
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

    def getGallons(self, appliance):
        if appliance.getApplianceName() == "Bath":
            return 30
        if appliance.getApplianceName() == "Shower":
            return 25
        if appliance.getApplianceName() == "Dishwasher":
            return 6
        if appliance.getApplianceName() == "Clothes Washer":
            return 20

    def getHotWaterPercentage(self, appliance):
        if appliance.getApplianceName() == "Bath":
            return 0.65
        if appliance.getApplianceName() == "Shower":
            return 0.65
        if appliance.getApplianceName() == "Dishwasher":
            return 1.00
        if appliance.getApplianceName() == "Clothes Washer":
            return 0.85


    def simulateUsage(self, appliance, day):
        print("\n" + "Toggling sensors for appliance " + appliance.getApplianceName())

        wakeTime = 18000            #5:00 AM
        leaveTime = 27000           #7:30 AM
        comeHomeTime = 57600        #4:00 PM
        sleepTime = 73800           #10:30 PM
        currentTime = wakeTime
        desiredTimeOn = self.getTimeOn(appliance, day)
        totalTimeOn = 0
        totalPowerUsage = 0
        totalPowerCost = 0
        totalWaterUsage = 0
        totalWaterCost = 0

        cleaningDays = ["Sat", "Sun", "Tues", "Thurs"]

        # Todo: The sensors turns on after leave time sometimes
        # Todo: Try to add something where the sensor does not turn off after leave time
        # Todo: Overhead Light and Bath Exhaust run less than they should
        # Todo: Extras: Make cooking appliances run in the PM instead? Make others 1/2 probability to run in AM/PM
        # Todo: May need to add 2 baths to kid bathroom and 2 showers to adult bathroom current each has one of each
        # Todo: May need to change weekend calculation of bath/shower usage (don't * 3?)
        # Todo: Update all usages and sensor states to their lists
        # Todo: calculate Daily Usage at the end of day
        # Todo: Clean this method up if need be. Good job \_o_/

        if appliance.getApplianceName() == "Refrigerator":
            startTime = self.convertSecondsToTime(0)
            appliance.getSensor().setSensorState(1)
            print("Turning on sensor at " + startTime)
            endTime = self.convertSecondsToTime(86400)
            print("Turning off sensor at " + endTime)
            totalPowerUsage = self.calculatePowerCost(appliance.getWatts(), desiredTimeOn)
            totalPowerCost = self.calculatePowerUsage(appliance.getWatts(), desiredTimeOn)
            totalTimeOn += desiredTimeOn

            print("\nTotal time on should be " + str(desiredTimeOn) + " but is " + str(totalTimeOn))
            print("Total Power Usage: %.2f kWh" % (totalPowerUsage))
            print("Total Power Cost: $%.2f" % (totalPowerCost))


        elif appliance.getApplianceName() == "Clothes Dryer":
            if day in cleaningDays:
                randomTime = random.randint(63000, 72000)
                startTime = self.convertSecondsToTime(randomTime)
                appliance.getSensor().setSensorState(1)
                print("Turning on sensor at " + startTime)
                endTime = self.convertSecondsToTime(randomTime + desiredTimeOn)
                appliance.getSensor().setSensorState(0)
                print("Turning off sensor at " + endTime)
                totalTimeOn += desiredTimeOn

                totalPowerUsage = self.calculatePowerCost(appliance.getWatts(), desiredTimeOn)
                totalPowerCost = self.calculatePowerUsage(appliance.getWatts(), desiredTimeOn)

                print("\nTotal time on should be " + str(desiredTimeOn) + " but is " + str(totalTimeOn))
                print("Total Power Usage: %.2f kWh" % (totalPowerUsage))
                print("Total Power Cost: $%.2f" % (totalPowerCost))


        elif appliance.getApplianceName() == "Clothes Washer":
            if day in cleaningDays:
                randomTime = random.randint(63000, 72000)
                startTime = self.convertSecondsToTime(randomTime)
                print("Turning on sensor at " + startTime)
                appliance.getSensor().setSensorState(1)
                endTime = self.convertSecondsToTime(randomTime + desiredTimeOn)
                appliance.getSensor().setSensorState(0)
                print("Turning off sensor at " + endTime)
                totalTimeOn += desiredTimeOn

                totalPowerUsage += self.calculatePowerCost(appliance.getWatts(), desiredTimeOn)
                totalPowerCost += self.calculatePowerUsage(appliance.getWatts(), desiredTimeOn)
                totalWaterUsage += self.calculateWaterUsage(appliance)
                totalWaterCost += self.calculateWaterCost(appliance)

            print("\nTotal time on should be " + str(desiredTimeOn) + " but is " + str(totalTimeOn))
            print("Total Power Usage: %.2f kWh" % (totalPowerUsage))
            print("Total Power Cost: $%.2f" % (totalPowerCost))
            print("Total Water Usage: %.2f kWh" % (totalWaterUsage))
            print("Total Water Cost: $%.2f" % (totalWaterCost))


        elif appliance.getApplianceName() == "Dishwasher":
            if day in cleaningDays:
                randomTime = random.randint(63000, 72000)
                startTime = self.convertSecondsToTime(randomTime)
                print("Turning on sensor at " + startTime)
                appliance.getSensor().setSensorState(1)
                endTime = self.convertSecondsToTime(randomTime + desiredTimeOn)
                appliance.getSensor().setSensorState(0)
                print("Turning off sensor at " + endTime)
                totalTimeOn += desiredTimeOn

                totalPowerUsage = self.calculatePowerCost(appliance.getWatts(), desiredTimeOn)
                totalPowerCost = self.calculatePowerUsage(appliance.getWatts(), desiredTimeOn)
                totalWaterUsage += self.calculateWaterUsage(appliance)
                totalWaterCost += self.calculateWaterCost(appliance)

            print("\nTotal time on should be " + str(desiredTimeOn) + " but is " + str(totalTimeOn))
            print("Total Power Usage: %.2f kWh" % (totalPowerUsage))
            print("Total Power Cost: $%.2f" % (totalPowerCost))
            print("Total Water Usage: %.2f kWh" % (totalWaterUsage))
            print("Total Water Cost: $%.2f" % (totalWaterCost))

        elif appliance.getApplianceName() == "Bath" or appliance.getApplianceName() == "Shower":
            if self.isWeekday(day):
                timeOn = desiredTimeOn
                randomTime = random.randint(18000, 21600)
                startTime = self.convertSecondsToTime(randomTime)
                print("Turning on sensor at " + startTime)
                appliance.getSensor().setSensorState(1)
                endTime = self.convertSecondsToTime(randomTime + timeOn)
                appliance.getSensor().setSensorState(0)
                print("Turning off sensor at " + endTime)
                totalTimeOn += timeOn

                totalWaterUsage += self.calculateWaterUsage(appliance)
                totalWaterCost += self.calculateWaterCost(appliance)

            else:
                timeOn = 3 * desiredTimeOn
                totalTimeOn += timeOn
                for i in range(3):
                    randomTime = self.generateRandomTime(currentTime, wakeTime, sleepTime)
                    startTime = self.convertSecondsToTime(randomTime)
                    appliance.getSensor().setSensorState(1)
                    print("Turning on sensor at " + startTime)
                    endTime = self.convertSecondsToTime(randomTime + desiredTimeOn)
                    appliance.getSensor().setSensorState(0)
                    print("Turning off sensor at " + endTime)
                    currentTime += randomTime + desiredTimeOn


                totalWaterUsage += self.calculateWaterUsage(appliance) * 3
                totalWaterCost += self.calculateWaterCost(appliance) * 3

            print("\nTotal time on should be " + str(desiredTimeOn) + " but is " + str(totalTimeOn))
            print("Total Water Usage: %.2f kWh" % (totalWaterUsage))
            print("Total Water Cost: $%.2f" % (totalWaterCost))

        else:
            if self.isWeekday(day):
                while wakeTime <= currentTime <= sleepTime:
                    if totalTimeOn < desiredTimeOn:
                        timeOn = random.randint(1, desiredTimeOn)
                        randomTime = self.generateRandomTime(currentTime, wakeTime, sleepTime)

                        if currentTime + randomTime + timeOn  < sleepTime:
                            if currentTime + timeOn > leaveTime:
                                timeOn = leaveTime - currentTime
                            else:
                                break

                            currentTime += randomTime

                            appliance.getSensor().setSensorState(1)
                            print(appliance.getSensor().getSensorState())
                            startTime = self.convertSecondsToTime(currentTime)
                            print("Turning on sensor at " + startTime)

                            currentTime += timeOn
                            totalTimeOn += timeOn

                            appliance.getSensor().setSensorState(0)
                            print(appliance.getSensor().getSensorState())
                            endTime = self.convertSecondsToTime(currentTime)
                            print("Turning off sensor at " + endTime)

                            usage = self.calculatePowerUsage(appliance.getWatts(), totalTimeOn)
                            totalPowerUsage += usage
                            cost = self.calculatePowerCost(appliance.getWatts(), totalTimeOn)
                            totalPowerCost += cost
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
                            print(appliance.getSensor().getSensorState())
                            startTime = self.convertSecondsToTime(currentTime)
                            print("Turning on sensor at " + startTime)

                            currentTime += timeOff

                            appliance.getSensor().setSensorState(0)
                            print(appliance.getSensor().getSensorState())
                            endTime = self.convertSecondsToTime(currentTime)
                            print("Turning off sensor at " + endTime)

                            usage = self.calculatePowerUsage(appliance.getWatts(), totalTimeOn)
                            totalPowerUsage += usage
                            cost = self.calculatePowerCost(appliance.getWatts(), totalTimeOn)
                            totalPowerCost += cost
                        else:
                            break
                    else:
                        break

            print("\nTotal time on should be " + str(desiredTimeOn) + " but is " + str(totalTimeOn))
            print("Total Power Usage: %.2f kWh" % (totalPowerUsage))
            print("Total Power Cost: $%.2f" % (totalPowerCost))




def simulate():
    s = Simulation()

    home = s.createHome()

    s.printHouseDetail()

    day = "Tues"

    print("\nSimulating power usage for appliances in rooms.\n")


    for room in home.getRooms():
        print("\n\n\nRoom: " + room.getRoomName())
        for appliance in room.getAppliances():
            if appliance.getApplianceName() == "Overhead Light":
                s.simulateUsage(appliance, day)
            if "Lamp" in appliance.getApplianceName():
                s.simulateUsage(appliance, day)
            if appliance.getApplianceName() == "Living Room TV":
                s.simulateUsage(appliance, day)
            if appliance.getApplianceName() == "Bedroom TV":
                s.simulateUsage(appliance, day)
            if appliance.getApplianceName() == "Bath Exhaust Fan":
                s.simulateUsage(appliance, day)
            if appliance.getApplianceName() == "Stove":
                s.simulateUsage(appliance, day)
            if appliance.getApplianceName() == "Oven":
                s.simulateUsage(appliance, day)
            if appliance.getApplianceName() == "Microwave":
                s.simulateUsage(appliance, day)
            if appliance.getApplianceName() == "Refrigerator":
                s.simulateUsage(appliance, day)
            if appliance.getApplianceName() == "Clothes Dryer":
                s.simulateUsage(appliance, day)
            if appliance.getApplianceName() == "Clothes Washer":
                s.simulateUsage(appliance, day)
            if appliance.getApplianceName() == "Dishwasher":
                s.simulateUsage(appliance, day)
            if appliance.getApplianceName() == "Shower":
                s.simulateUsage(appliance, day)
            if appliance.getApplianceName() == "Bath":
                s.simulateUsage(appliance, day)


simulate()









