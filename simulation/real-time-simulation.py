import random

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
            print("\n" + room.getRoomName() + ": \n")
            for appliance in room.getAppliances():
                print(appliance.toString())

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

