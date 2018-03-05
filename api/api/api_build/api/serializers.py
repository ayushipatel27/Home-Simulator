from rest_framework import serializers 

from api_build.models import Appliances, Dailyusage, Energyusage, Hvacusage, Rooms, Sensors, Waterusage, Weather

# Converts to JSON
# Validates for data passed

class AppliancesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Appliances
		fields = [
			'applianceid',
			'sensorid',
		    'powerusage',
		    'powerrate',
		]

class DailyusageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Dailyusage
		fields = [
			'date',
			'totalwaterusage',
			'totalpowerusage',
			'totalpowercost',
			'totalwatercost',
			'totalhvacusage',
			'totalhvaccost',
		]

class EnergyusageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Energyusage
		fields = [
			'timestamp',
			'sensorid',
			'endtimestamp',
			'usage',
			'cost',
		]

class HvacusageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Hvacusage
		fields = [
			'timestamp',
			'sensorid',
			'endtimestamp',
			'usage',
			'cost',
			'temperature',
		]

class RoomsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rooms
		fields = [
			'roomid',
			'roomname',
		]

class SensorsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sensors
		fields = [
			'sensorid',
			'sensorname',
			'sensorstate',
			'roomid',
		]

class WaterusageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Waterusage
		fields = [
			'timestamp',
			'sensorid',
			'endtimestamp',
			'usage',
			'cost',
		]

class WeatherSerializer(serializers.ModelSerializer):
	class Meta:
		model = Weather
		fields = [
			'timestamp',
			'temperature',
			'precipitation',
			'chanceofprecipitation',
			'state',
		]


