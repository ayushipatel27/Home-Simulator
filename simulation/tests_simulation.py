import unittest
from datetime import date, datetime, time, timedelta

from historic_simulation import Appliance as Appliance
from historic_simulation import Home as Home
from historic_simulation import Room as Room
from historic_simulation import Sensor as Sensor
from historic_simulation import Simulation as Simulation


class SensorTest(unittest.TestCase):
    def setUp(self):
        self.testSensor = Sensor(0, "Test Sensor", 0)
        print("setUp executed!")

    def test_Sesnor(self):
        sensor = Sensor(0, "Test Sensor", 0)
        self.assertEqual(sensor, self.testSensor)

    def tearDown(self):
        self.testSesnor = None
        print("tearDown executed!")


class ApplianceTest(unittest.TestCase):
    def setUp(self):
        self.testAppliance = Appliance(0, "Test Appliance", 30)

    def test_Appliance(self):
        appliance = Appliance(0, "Test Appliance", 30)
        self.assertEqual(appliance, self.testAppliance)

    def tearDown(self):
        self.testAppliance = None


class RoomTest(unittest.TestCase):
    def setUp(self):
        self.testRoom = Room(0, "Test Room")

    def test_Appliance(self):
        room = Room(0, "Test Room")
        self.assertEqual(room, self.testRoom)

    def tearDown(self):
        self.testRoom = None


class HomeTest(unittest.TestCase):
    def setUp(self):
        self.testHome = Home()
        self.testHome.addRooms([10, 20, 30])

    def test_Home(self):
        home = Home()
        home.addRooms([10, 20, 30])
        self.assertEqual(home, self.testHome)

    def tearDown(self):
        self.testHome = None


class SimulationTest(unittest.TestCase):

    def setUp(self):
        self.Sim = Simulation()
        self.home = Home()
        self.hotWaterAppliances = [Appliance(0, "Bath", 0), Appliance(
            0, "Shower", 0), Appliance(0, "Dishwasher", 0), Appliance(
            0, "Clothes Washer", 0)]
        self.rooms = []

    def testaddRooms(self):
        roomNames = [
            "Master Bedroom", "Kid 1 Bedroom", "Kid 2 Bedroom",
            "Master Bathroom", "Kids Bathroom", "Garage", "Living Room",
            "Kitchen", "Laundry Room"]
        rooms = [Room(1, "Master Bedroom"),
                 Room(2, "Kid 1 Bedroom"),
                 Room(3, "Kid 2 Bedroom"),
                 Room(4, "Master Bathroom"),
                 Room(5, "Kids Bathroom"),
                 Room(6, "Garage"),
                 Room(7, "Living Room"),
                 Room(8, "Kitchen"),
                 Room(9, "Laundry Room")
                 ]
        self.Sim.home.addRooms(rooms)
        for i in self.Sim.home.getRooms():
            roomName = i.getRoomName()
            self.assertTrue(roomName in roomNames)

    def testaddAppliances(self):
        appliances_to_add = ["Overhead Light",
                             "Bath Exhaust Fan", "Bath", "Shower"]
        # There should be a single addRoom sunction...
        self.Sim.home.addRoom(Room(5, "Kids Bathroom"))
        self.Sim.home.getRoom("Kids Bathroom").addAppliances(
            [Appliance(21, "Overhead Light", 60), Appliance(22, "Bath Exhaust Fan", 30), Appliance(23, "Bath", 0),
             Appliance(24, "Shower", 0)])

        room_appliances = self.Sim.home.getRoom(
            "Kids Bathroom").getAppliances()

        for (appl, room_appl) in zip(appliances_to_add, room_appliances):
            room_appl_name = room_appl.getApplianceName()
            self.assertEqual(appl, room_appl_name)

    def testaddPowerUsage(self):
        valid_powerUsage = []
        startTime, sensorId, endTime, usage, cost = 0, 0, 0, 40.0, 180.0
        valid_powerUsage.append({'timestamp': startTime,
                                 'sensorid': sensorId,
                                 'endtimestamp': endTime,
                                 'usage': usage,
                                 'cost': cost})
        self.Sim.addPowerUsage(startTime, sensorId, endTime, usage, cost)
        actual_PowerUsage = self.Sim.powerUsages
        self.assertEqual(valid_powerUsage, actual_PowerUsage)

    def testaddWaterUsage(self):
        valid_waterUsage = []
        startTime, sensorId, endTime, usage, cost = 0, 0, 0, 40.0, 180.0
        valid_waterUsage.append({'timestamp': startTime,
                                 'sensorid': sensorId,
                                 'endtimestamp': endTime,
                                 'usage': usage,
                                 'cost': cost})

        self.Sim.addWaterUsage(startTime, sensorId, endTime, usage, cost)
        actual_waterUsage = self.Sim.waterUsages
        self.assertEqual(valid_waterUsage, actual_waterUsage)

    def testaddHvacUsage(self):
        valid_hvacUsage = []
        startTime, sensorId, endTime, usage, cost, temp = 0, 0, 0, 40.0, 180.0, 70
        valid_hvacUsage.append({'timestamp': startTime,
                                'sensorid': sensorId,
                                'endtimestamp': endTime,
                                'usage': usage,
                                'cost': cost,
                                'temperature': temp})

        self.Sim.addHvacUsage(sensorId, startTime, endTime, temp, usage, cost)
        actual_hvacUsage = self.Sim.hvacUsages
        self.assertEqual(valid_hvacUsage, actual_hvacUsage)

    def testaddDailyUsage(self):
        valid_dailyUsage = []
        date_of, totalWaterUsage, totalPowerUsage, totalHvacUsage = datetime(
            2015, 1, 1), 100.0, 50.0, 100
        totalPowerCost, totalWaterCost, totalhvaccost = 100.9, 65.00, 0.1
        valid_dailyUsage.append({'date': date_of.strftime("%Y-%m-%d"),
                                 'totalwaterusage': int(totalWaterUsage),
                                 'totalpowerusage': int(totalPowerUsage),
                                 'totalpowercost': int(totalPowerCost),
                                 'totalwatercost':  int(totalWaterCost),
                                 'totalhvacusage': int(totalHvacUsage),
                                 'totalhvaccost': int(totalhvaccost)})

        self.Sim.addDailyUsage(date_of, totalWaterUsage, totalPowerUsage,
                               totalHvacUsage, totalPowerCost, totalWaterCost,
                               totalhvaccost)

        actual_dailyUsage = self.Sim.dailyUsages
        self.assertEqual(valid_dailyUsage, actual_dailyUsage)

    def testisWeekday(self):
        weekdays = [1, 2, 3, 4]
        weekends = [5, 6, 7, 8]
        for (weekday, weekend) in zip(weekdays, weekends):
            true_method_results = self.Sim.isWeekday(weekday)
            false_method_results = self.Sim.isWeekday(weekend)

            self.assertTrue(true_method_results)
            self.assertFalse(false_method_results)

    def testgetGallons(self):
        wrong_Gallons = [1.0, 66, 13, 30]
        correct_Gallons = [30, 25, 6, 20]
        # Why are these hardcoded?
        li = zip(self.hotWaterAppliances, correct_Gallons,
                 wrong_Gallons)
        for (app, correctGallon, incorrectGallon) in li:
            gallons = self.Sim.getGallons(appliance=app)
            self.assertEqual(gallons, correctGallon)
            self.assertNotEqual(gallons, incorrectGallon)

    def testgetHotWaterPercentage(self):
        wrong_HotWaterPercentages = [1.0, 0.99, 0.10, 0.55]
        correct_HotWaterPercentage = [0.65, 0.65, 1.00, 0.85]
        li = zip(self.hotWaterAppliances, correct_HotWaterPercentage,
                 wrong_HotWaterPercentages)
        for (app, correctPercent, incorrectPercent) in li:
            p = self.Sim.getHotWaterPercentage(appliance=app)
            self.assertEqual(p, correctPercent)
            self.assertNotEqual(p, incorrectPercent)

    def tearDown(self):
        self.Sim = None
        self.hotWaterAppliances = None


if __name__ == "__main__":
    unittest.main()
