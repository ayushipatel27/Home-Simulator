from rest_framework import serializers 

from api_build.models import Appliances, Dailyusage, Powerusage, Hvacusage, Rooms, Sensors, Waterusage, Weather, Livewaterusage, Livepowerusage

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

class HvacusageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Hvacusage
		fields = [
			'hvacusageid',
			'timestamp',
			'sensorid',
			'endtimestamp',
			'usage',
			'cost',
			'temperature',
		]

class LivepowerusageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Livepowerusage
		fields = [
			'livepowerusageid',
			'timestamp',
			'sensorids',
			'endtimestamp',
			'usage',
			'cost',
		]

class LivewaterusageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Livewaterusage
		fields = [
			'livewaterusageid',
			'timestamp',
			'sensorids',
			'endtimestamp',
			'usage',
			'cost',
		]

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
			'waterusageid',
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
			'weatherid',
			'timestamp',
			'temperature',
			'precipitation',
			'chanceofprecipitation',
			'state',
		]


