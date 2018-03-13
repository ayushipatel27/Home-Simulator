import simpy, random
from datetime import timedelta, time

# Create Power Usage objects to update power usage tables.
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

        for room in rooms[0:3]:
            room.addAppliances({appliances[0]: 1, appliances[1]: 2, appliances[3]: 1, appliances[14]: 2})

        for room in rooms[3:5]:
            room.addAppliances({appliances[0]: 1, appliances[4]: 1})

        rooms[5].addAppliances({appliances[13]: 2, appliances[14]: 1, appliances[12]: 1})
        rooms[6].addAppliances({appliances[0]: 1, appliances[1]: 2, appliances[2]: 1, appliances[13]: 2, appliances[14]: 2, appliances[15]: 1})
        rooms[7].addAppliances({appliances[0]: 1, appliances[5]: 1, appliances[6]: 1, appliances[7]: 1, appliances[8]: 1, appliances[9]: 1, appliances[13]: 1})
        rooms[8].addAppliances({appliances[10]: 1, appliances[11]: 1})

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


    def generateRandomTime(self, currentTime, startTime, endTime):
        randomTime = 0
        while startTime <= currentTime <= endTime:
            randomTime = random.randint(currentTime, currentTime+1800)
            if currentTime < randomTime:
                break
        return randomTime - currentTime


    def startUsage(self, appliance, durationOn, startTime, endTime, totalTime, totalTimeOn):
        while startTime <= totalTime <= endTime:
            timeOn = random.randint(1, durationOn)
            timeOff = random.randint(1, durationOn)
            randomTime = self.generateRandomTime(totalTime, startTime, endTime)
            if totalTime + randomTime + timeOn + timeOff < endTime:
                totalTime += randomTime + timeOn
                totalTimeOn += timeOn
                appliance.getSensor().setSensorState(1)
                print("Turning on sensor at " + str(self.convertSecondsToTime(totalTime)))

                totalTime += timeOff
                appliance.getSensor().setSensorState(0)
                print("Turning off sensor at " + str(self.convertSecondsToTime(totalTime)))
            else:
                break
        return totalTimeOn

    def simulatePowerUsage(self, appliance, durationOn, day):
        print("\n" + "Toggling sensors for appliance " + appliance.getApplianceName())
        days = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]

        wakeTime = 18000            #5:00 AM
        leaveTime = 27000           #7:30 AM
        comeHomeTime = 57600        #4:00 PM
        sleepTime = 73800           #10:30 PM
        totalTime = wakeTime
        totalTimeOn = 0
        totalUsage = 0
        totalCost = 0
        r = random.random()

        # 1/2 probability appliance will turn on in morning/night
        if day in days[0:5]:
            while totalTimeOn < durationOn:
                totalTimeOn = self.startUsage(appliance, durationOn, wakeTime, leaveTime, totalTime, totalTimeOn)
                usage = self.calculatePowerUsage(appliance.getWatts(), totalTimeOn)
                totalUsage += usage
                cost = self.calculatePowerCost(appliance.getWatts(), totalTimeOn)
                totalCost += cost

                totalTimeOn = self.startUsage(appliance, durationOn, comeHomeTime, sleepTime, totalTime, totalTimeOn)
                usage = self.calculatePowerUsage(appliance.getWatts(), totalTimeOn)
                totalUsage += usage
                cost = self.calculatePowerCost(appliance.getWatts(), totalTimeOn)
                totalCost += cost
        else:
            while totalTimeOn < durationOn:
                totalTimeOn = self.startUsage(appliance, durationOn, wakeTime, sleepTime, totalTime, totalTimeOn)
                usage = self.calculatePowerUsage(appliance.getWatts(), totalTimeOn)
                totalUsage += usage
                cost = self.calculatePowerCost(appliance.getWatts(), totalTimeOn)
                totalCost += cost

        print("\nTotal time on should be " + str(timedelta(seconds=durationOn)) + " but is " + str(timedelta(seconds=totalTimeOn)))
        print("Total Usage: %.2f watts" % (totalUsage))
        print("Total Cost: $%.2f" % (totalCost))



def simulate():
    s = Simulation()

    sensors = s.createSensors()
    appliances = s.createAppliances(sensors)
    rooms = s.createRooms(appliances)
    home = s.createHome(rooms)

    s.printHouseDetail(home, rooms, appliances, sensors)

    days = ["Mon","Tues","Wed","Thurs","Fri","Sat","Sun"]
    day = "Mon"

    print("\nSimulating power usage for appliances in rooms.\n")


    for room in rooms:
        print("\nRoom: " + room.getRoomName())
        for appliance in room.getAppliances():
            if appliance.getApplianceName() == "Overhead Light":
                if day in days[0:5]:
                    s.simulatePowerUsage(appliance, random.randint(1, 25200), day)
                elif day in days[5:7]:
                    s.simulatePowerUsage(appliance, random.randint(1, 86400), day)
            if appliance.getApplianceName() == "Lamp":
                if day in days[0:5]:
                    s.simulatePowerUsage(appliance, random.randint(1, 25200), day)
                elif day in days[5:7]:
                    s.simulatePowerUsage(appliance, random.randint(1, 86400), day)
            if appliance.getApplianceName() == "Living Room TV":
                if day in days[0:5]:
                    s.simulatePowerUsage(appliance, 14400, day)
                elif day in days[5:7]:
                    s.simulatePowerUsage(appliance, 28800, day)
            if appliance.getApplianceName() == "Bedroom TV":
                if day in days[0:5]:
                    s.simulatePowerUsage(appliance, 7200, day)
                elif day in days[5:7]:
                    s.simulatePowerUsage(appliance, 14400, day)
            if appliance.getApplianceName() == "Bath Exhaust Fan":
                if day in days[0:5]:
                    s.simulatePowerUsage(appliance, random.randint(1, 25200), day)
                elif day in days[5:7]:
                    s.simulatePowerUsage(appliance, random.randint(1, 86400), day)
            if appliance.getApplianceName() == "Stove":
                if day in days[0:5]:
                    s.simulatePowerUsage(appliance, 900, day)
                elif day in days[5:7]:
                    s.simulatePowerUsage(appliance, 1800, day)
            if appliance.getApplianceName() == "Oven":
                if day in days[0:5]:
                    s.simulatePowerUsage(appliance, 2700, day)
                elif day in days[5:7]:
                    s.simulatePowerUsage(appliance, 3600, day)
            if appliance.getApplianceName() == "Microwave":
                if day in days[0:5]:
                    s.simulatePowerUsage(appliance, 1200, day)
                elif day in days[5:7]:
                    s.simulatePowerUsage(appliance, 1800, day)
            if appliance.getApplianceName() == "Refrigerator":
                if day in days[0:5]:
                    s.simulatePowerUsage(appliance, random.randint(1, 25200), day)
                elif day in days[5:7]:
                    s.simulatePowerUsage(appliance, random.randint(1, 86400), day)

# need to have it where random time isn't picked between all day for duration on
# while lopp for until totalTimeOn < duration is running again and it shouldn't
simulate()








