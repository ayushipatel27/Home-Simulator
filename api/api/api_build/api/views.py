# Generic

from django.db.models import Q
from rest_framework import generics, mixins

from api_build.models import Appliances, Dailyusage, Energyusage, Hvacusage, Rooms, Sensors, Waterusage, Weather
from .serializers import AppliancesSerializer, DailyusageSerializer, EnergyusageSerializer, HvacusageSerializer, RoomsSerializer, SensorsSerializer, WaterusageSerializer, WeatherSerializer



#######################################################################
#                            RUD VIEWS                                #
#######################################################################

class AppliancesRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field     = 'applianceid'
	serializer_class = AppliancesSerializer

	def get_queryset(self):
		return Appliances.objects.all()

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def patch(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)



class DailyusageRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field     = 'dailyusageid'
	serializer_class = DailyusageSerializer

	def get_queryset(self):
		return Dailyusage.objects.all()

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def patch(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)



class EnergyusageRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field     = 'energyusageid'
	serializer_class = EnergyusageSerializer

	def get_queryset(self):
		return Energyusage.objects.all()

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def patch(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)



class HvacusageRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field     = 'hvacusageid'
	serializer_class = HvacusageSerializer

	def get_queryset(self):
		return Hvacusage.objects.all()

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def patch(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)



class RoomsRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field     = 'roomid'
	serializer_class = RoomsSerializer

	def get_queryset(self):
		return Rooms.objects.all()

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def patch(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)



class SensorsRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field     = 'sensorid'
	serializer_class = SensorsSerializer

	def get_queryset(self):
		return Sensors.objects.all()

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def patch(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)



class WaterusageRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field     = 'waterusageid'
	serializer_class = WaterusageSerializer

	def get_queryset(self):
		return Waterusage.objects.all()

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def patch(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)



class WeatherRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field     = 'weatherid'
	serializer_class = WeatherSerializer

	def get_queryset(self):
		return Weather.objects.all()

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def patch(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)



#######################################################################
#                       LIST CREATE VIEWS                             #
#######################################################################

class AppliancesAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	serializer_class = AppliancesSerializer

	def get_queryset(self):
		qs = Appliances.objects.all()
		query = self.request.GET.get("q")
		if query is not None:
			qs = qs.filter(Q(applianceid__icontains=query)|
						   Q(sensorid__sensorid__icontains=query)|
						   Q(powerusage__icontains=query)|
						   Q(powerrate__icontains=query)).distinct()
		return qs

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def perform_create(self, serializer):
		serializer.save(applianceid=self.request.applianceid, sensorid=self.request.sensorid)



class DailyusageAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	serializer_class = DailyusageSerializer

	def get_queryset(self):
		qs = Dailyusage.objects.all()
		query = self.request.GET.get("q")
		if query is not None:
			qs = qs.filter(Q(date__icontains=query)|
						   Q(totalwaterusage__icontains=query)|
						   Q(totalpowerusage__icontains=query)|
						   Q(totalpowercost__icontains=query)|
						   Q(totalwatercost__icontains=query)|
						   Q(totalhvacusage__icontains=query)|
						   Q(totalhvaccost__icontains=query)).distinct()
		return qs

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def perform_create(self, serializer):
		serializer.save(date=self.request.date)



class EnergyusageAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	serializer_class = EnergyusageSerializer

	def get_queryset(self):
		qs = Energyusage.objects.all()
		query = self.request.GET.get("q")
		if query is not None:
			qs = qs.filter(Q(timestamp__icontains=query)|
						   Q(sensorid__icontains=query)|
						   Q(endtimestamp__icontains=query)|
						   Q(usage__icontains=query)|
						   Q(cost__icontains=query)).distinct()
		return qs

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def perform_create(self, serializer):
		serializer.save(timestamp=self.request.timestamp)



class HvacusageAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	serializer_class = HvacusageSerializer

	def get_queryset(self):
		qs = Hvacusage.objects.all()
		query = self.request.GET.get("q")
		if query is not None:
			qs = qs.filter(Q(timestamp__icontains=query)|
						   Q(sensorid__icontains=query)|
						   Q(endtimestamp__icontains=query)|
						   Q(usage__icontains=query)|
						   Q(cost__icontains=query)|
						   Q(temperature__icontains=query)).distinct()
		return qs

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def perform_create(self, serializer):
		serializer.save(timestamp=self.request.timestamp)



class RoomsAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	serializer_class = RoomsSerializer

	def get_queryset(self):
		qs = Rooms.objects.all()
		query = self.request.GET.get("q")
		if query is not None:
			qs = qs.filter(Q(roomid__icontains=query)|
						   Q(roomname__icontains=query)).distinct()
		return qs

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def perform_create(self, serializer):
		serializer.save(roomid=self.request.roomid)



class SensorsAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	serializer_class = SensorsSerializer

	def get_queryset(self):
		qs = Sensors.objects.all()
		query = self.request.GET.get("q")
		if query is not None:
			qs = qs.filter(Q(sensorid__icontains=query)|
						   Q(sensorname__icontains=query)|
						   Q(sensorstate__icontains=query)|
						   Q(roomid__roomid__icontains=query)).distinct()
		return qs

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def perform_create(self, serializer):
		serializer.save(sensorid=self.request.sensorid, roomid=self.request.roomid)



class WaterusageAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	serializer_class = WaterusageSerializer

	def get_queryset(self):
		qs = Waterusage.objects.all()
		query = self.request.GET.get("q")
		if query is not None:
			qs = qs.filter(Q(timestamp__icontains=query)|
						   Q(sensorid__icontains=query)|
						   Q(endtimestamp__icontains=query)|
						   Q(usage__icontains=query)|
						   Q(cost__icontains=query)).distinct()
		return qs

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def perform_create(self, serializer):
		serializer.save(timestamp=self.request.timestamp)



class WeatherAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	serializer_class = WeatherSerializer

	def get_queryset(self):
		qs = Weather.objects.all()
		query = self.request.GET.get("q")
		if query is not None:
			qs = qs.filter(Q(timestamp__icontains=query)|
						   Q(temperature__icontains=query)|
						   Q(precipitation__icontains=query)|
						   Q(chanceofprecipitation__icontains=query)|
						   Q(state__icontains=query)).distinct()
		return qs

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def perform_create(self, serializer):
		serializer.save(timestamp=self.request.timestamp)


