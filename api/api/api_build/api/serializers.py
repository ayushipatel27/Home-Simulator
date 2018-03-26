from rest_framework import serializers 

from api_build.models import Appliances, Dailyusage, Powerusage, Hvacusage, Rooms, Sensors, Waterusage, Weather

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
		    'appliancename',
		]
		read_only_fields = ['applianceid', 'sensorid']

class DailyusageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Dailyusage
		fields = [
			'dailyusageid',
			'date',
			'totalwaterusage',
			'totalpowerusage',
			'totalpowercost',
			'totalwatercost',
			'totalhvacusage',
			'totalhvaccost',
		]
		read_only_fields = ['applianceid', 'sensorid']

class HvacusageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Hvacusage
		fields = [
			'hvacid',
			'timestamp',
			'sensorid',
			'endtimestamp',
			'usage',
			'cost',
			'temperature',
		]
		read_only_fields = ['timestamp']

class PowerusageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Powerusage
		fields = [
		    'energyusageid',
			'timestamp',
			'sensorid',
			'endtimestamp',
			'usage',
			'cost',
		]
		read_only_fields = ['energyusageid']

class RoomsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rooms
		fields = [
			'roomid',
			'roomname',
		]
		read_only_fields = ['roomid']

class SensorsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sensors
		fields = [
			'sensorid',
			'sensorname',
			'sensorstate',
			'roomid',
		]
		read_only_fields = ['sensorid', 'roomid']

class WaterusageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Waterusage
		fields = [
			'waterid',
			'timestamp',
			'sensorid',
			'endtimestamp',
			'usage',
			'cost',
		]
		read_only_fields = ['timestamp']

class WeatherSerializer(serializers.ModelSerializer):
	class Meta:
		model = Weather
		fields = [
			'weatherid',
			'timestamp',
			'temperature',
			'precipitation',
			'chanceofprecipitation',
			'state',
		]
		read_only_fields = ['timestamp']


