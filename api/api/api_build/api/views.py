# Generic


from rest_framework import generics

from api_build.models import Appliances, Dailyusage, Energyusage, Hvacusage, Rooms, Sensors, Waterusage, Weather
from .serializers import AppliancesSerializer, DailyusageSerializer, EnergyusageSerializer, HvacusageSerializer, RoomsSerializer, SensorsSerializer, WaterusageSerializer, WeatherSerializer

class AppliancesRudView(generics.ListCreateAPIView):
	#lookup_field     = 'applianceid'
	serializer_class = AppliancesSerializer

	def get_queryset(self):
		return Appliances.objects.all()



class DailyusageRudView(generics.ListCreateAPIView):
	serializer_class = DailyusageSerializer

	def get_queryset(self):
		return Dailyusage.objects.all()



class EnergyusageRudView(generics.ListCreateAPIView):
	serializer_class = EnergyusageSerializer

	def get_queryset(self):
		return Energyusage.objects.all()



class HvacusageRudView(generics.ListCreateAPIView):
	serializer_class = HvacusageSerializer

	def get_queryset(self):
		return Hvacusage.objects.all()



class RoomsRudView(generics.ListCreateAPIView):
	serializer_class = RoomsSerializer

	def get_queryset(self):
		return Rooms.objects.all()



class SensorsRudView(generics.ListCreateAPIView):
	serializer_class = SensorsSerializer

	def get_queryset(self):
		return Sensors.objects.all()



class WaterusageRudView(generics.ListCreateAPIView):
	serializer_class = WaterusageSerializer

	def get_queryset(self):
		return Waterusage.objects.all()



class WeatherRudView(generics.ListCreateAPIView):
	serializer_class = WeatherSerializer

	def get_queryset(self):
		return Weather.objects.all()


