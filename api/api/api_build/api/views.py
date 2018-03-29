# Generic

from django.db.models import Q
from rest_framework import generics, mixins, viewsets
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from .housestate import HouseState
from datetime import datetime, timedelta, time, date
from django.db.models import Sum
import json
from rest_framework.generics import UpdateAPIView

from api_build.models import ( Appliances, 
							   Dailyusage, 
							   Powerusage, 
							   Hvacusage, 
							   Rooms, 
							   Sensors, 
							   Waterusage, 
							   Weather,
                               Livewaterusage,
                               Livepowerusage
							 )

from .serializers import ( AppliancesSerializer, 
						   DailyusageSerializer, 
						   PowerusageSerializer, 
						   HvacusageSerializer, 
						   RoomsSerializer, 
						   SensorsSerializer, 
						   WaterusageSerializer, 
						   WeatherSerializer,
                           LivepowerusageSerializer,
                           LivewaterusageSerializer
						 )

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


class HvacusageRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field     = 'hvacusageid'
	serializer_class = HvacusageSerializer

	def get_queryset(self):
		return Hvacusage.objects.all()

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def patch(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)


class PowerusageRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field     = 'Powerusageid'
	serializer_class = PowerusageSerializer

	def get_queryset(self):
		return Powerusage.objects.all()

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

		instance = self.get_object()
		instance.roomname = request.data.get("roomname")
		instance.save()

		serializer = self.get_serializer(instance)
		serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)

		return self.partial_update(request, *args, **kwargs)


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
#                   GET SPECIFIED COLLECTIONS                         #
#######################################################################


class GetSensors(generics.ListAPIView):
	serializer_class = SensorsSerializer

	def get_queryset(self):

		roomid = self.kwargs['roomid']
		return Sensors.objects.filter(roomid=roomid)

class GetAppliances(generics.ListAPIView):
	serializer_class = AppliancesSerializer

	def get_queryset(self):

		sensorid = self.kwargs['sensorid']
		return Appliances.objects.filter(sensorid=sensorid)


class GetSensorsTurnedOn(generics.ListAPIView):
    serializer_class = SensorsSerializer

    def get_queryset(self):

        return Sensors.objects.filter(sensorstate=1)


def GetWeekOfPower(request):

    power_dict = []

    one_week_ago = date.today() - timedelta(days=7)
    today = date.today()

    powerObj = Powerusage.objects.filter(endtimestamp__isnull=False, timestamp__gte=one_week_ago, endtimestamp__lte=today)

    power = serializers.serialize('json', powerObj)
    powerusage = json.loads(power)

    for p in powerusage:
        power_dict.append(p['fields'])

    return HttpResponse(json.dumps(power_dict, indent=4, sort_keys=True), content_type="application/json")

def GetWeekOfWater(request):

    water_dict = []

    one_week_ago = date.today() - timedelta(days=7)
    today = date.today()

    waterObj = Waterusage.objects.filter(endtimestamp__isnull=False, timestamp__gte=one_week_ago, endtimestamp__lte=today)

    water = serializers.serialize('json', waterObj)
    waterusage = json.loads(water)

    for p in waterusage:
        water_dict.append(p['fields'])

    return HttpResponse(json.dumps(water_dict, indent=4, sort_keys=True), content_type="application/json")

def GetMonthOfPower(request):

    power_dict = []

    one_month_ago = date.today() - timedelta(days=30)
    today = date.today()

    powerObj = Powerusage.objects.filter(endtimestamp__isnull=False, timestamp__gte=one_month_ago, endtimestamp__lte=today)

    power = serializers.serialize('json', powerObj)
    powerusage = json.loads(power)

    for p in powerusage:
        power_dict.append(p['fields'])

    return HttpResponse(json.dumps(power_dict, indent=4, sort_keys=True), content_type="application/json")

def GetMonthOfWater(request):

    water_dict = []

    one_month_ago = date.today() - timedelta(days=30)
    today = date.today()

    waterObj = Waterusage.objects.filter(endtimestamp__isnull=False, timestamp__gte=one_month_ago, endtimestamp__lte=today)

    water = serializers.serialize('json', waterObj)
    waterusage = json.loads(water)

    for p in waterusage:
        water_dict.append(p['fields'])

    return HttpResponse(json.dumps(water_dict, indent=4, sort_keys=True), content_type="application/json")


#######################################################################
#                       LIST VIEWS                                    #
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
						   Q(powerrate__icontains=query)|
						   Q(appliancename__icontains=query)).distinct()
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


class PowerusageAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	serializer_class = PowerusageSerializer

	def get_queryset(self):
		qs = Powerusage.objects.all()
		query = self.request.GET.get("q")
		if query is not None:
			qs = qs.filter(Q(energyusageid__icontains=query)|
			               Q(timestamp__icontains=query)|
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


#######################################################################
#                       UPDATE STATES                                 #
#######################################################################

@csrf_exempt
def UpdateHouseState(request):
    if request.method=='POST':
        #data = json.loads(request.body)

        GetCurrentHouseState()

        #print("\n" + str(data) + "\n")

        # for i in data:
        #     tmp = Rooms.objects.get(roomid=i['roomid'])
        #     tmp.roomname = i['roomname']
        #     tmp.save()

    return HttpResponse('')


def GetCurrentHouseState(request):

    for room_key, room_elem in HouseState['home']['rooms'].items():

        for sensor_key, sensor_elem in room_elem['sensors'].items():

            dbSensor = Sensors.objects.get(sensorid = sensor_elem['sensor id'])
            sensor_elem['state'] = dbSensor.sensorstate

            for appliance_key, appliance_elem in sensor_elem['appliances'].items():

                    dbAppliance = Appliances.objects.get(applianceid = sensor_elem['sensor id'])
                    appliance_elem['usage'] = dbAppliance.powerusage


    # GET CURRENTLY ACTIVE POWER, WATER, AND HVAC
    powerObj = Livepowerusage.objects.latest('livepowerusageid')
    power = serializers.serialize('json', [powerObj])
    powerusage = json.loads(power)

    havacObj = Hvacusage.objects.latest('hvacusageid')
    hvac = serializers.serialize('json', [havacObj])
    hvacusage = json.loads(hvac)

    waterObj = Livewaterusage.objects.latest('livewaterusageid')
    water = serializers.serialize('json', [waterObj])
    waterusage = json.loads(water)

    weatherObj = Weather.objects.latest('weatherid')
    weath = serializers.serialize('json', [weatherObj])
    weather = json.loads(weath)

    HouseState['home']['hvacusage']  = hvacusage[0]['fields']
    HouseState['home']['waterusage'] = waterusage[0]['fields']
    HouseState['home']['powerusage'] = powerusage[0]['fields']
    HouseState['home']['weather']    = weather[0]['fields']

    return HttpResponse(json.dumps(HouseState, indent=4, sort_keys=True), content_type="application/json")
    

#######################################################################
#                       INSERT STATES                                 #
#######################################################################

@csrf_exempt
def InsertAppliances(request):
    if request.method=='POST':
        data = json.loads(request.body)

        for i in data:
            sensor = Sensors.objects.get(sensorid=i['sensorid'])
            appliance = Appliances.objects.create(sensorid       = sensor, 
            									  powerusage     = i['powerusage'], 
            									  powerrate      = i['powerrate'], 
            									  appliancename  = i['appliancename'])
            appliance.save()

    return HttpResponse('')


@csrf_exempt
def InsertDailyusage(request):
    if request.method=='POST':
        data = json.loads(request.body)

        for i in data:
            dailyusage = Dailyusage.objects.create(date            = i['date'],
											       totalwaterusage = i['totalwaterusage'],
											       totalpowerusage = i['totalpowerusage'],
											       totalpowercost  = i['totalpowercost'],
											       totalwatercost  = i['totalwatercost'],
											       totalhvacusage  = i['totalhvacusage'],
											       totalhvaccost   = i['totalhvaccost'])
            dailyusage.save()

    return HttpResponse('')


@csrf_exempt
def InsertPowerusage(request):
    if request.method=='POST':
        data = json.loads(request.body)

        for i in data:
            powerusage = Powerusage.objects.create(timestamp    = i['timestamp'],
											       sensorid     = i['sensorid'],
											       endtimestamp = i['endtimestamp'],
											       usage        = i['usage'],
											       cost         = i['cost'])
            powerusage.save()

    return HttpResponse('')

@csrf_exempt
def InsertPowerusageNoEndtime(request):
    if request.method=='POST':
        data = json.loads(request.body)

        for i in data:
            powerusage = Powerusage.objects.create(timestamp    = i['timestamp'],
                                                   sensorid     = i['sensorid'],
                                                   usage        = i['usage'],
                                                   cost         = i['cost'])
            powerusage.save()

    return HttpResponse('')


@csrf_exempt
def InsertHvacusage(request):
    if request.method=='POST':
        data = json.loads(request.body)

        for i in data:
            hvacusage = Hvacusage.objects.create(timestamp      = i['timestamp'],
											     endtimestamp   = i['endtimestamp'],
											     usage          = i['usage'],
											     cost           = i['cost'],
											     temperature    = i['temperature'])
            hvacusage.save()

    return HttpResponse('')

@csrf_exempt
def InsertHvacusageNoEndtime(request):
    if request.method=='POST':
        data = json.loads(request.body)

        for i in data:
            hvacusage = Hvacusage.objects.create(timestamp      = i['timestamp'],
                                                 usage          = i['usage'],
                                                 cost           = i['cost'],
                                                 temperature    = i['temperature'])
            hvacusage.save()

    return HttpResponse('')


@csrf_exempt
def InsertRooms(request):
    if request.method=='POST':
        data = json.loads(request.body)

        for i in data:
            room = Rooms.objects.create(roomname=i['roomname'])
            room.save()

    return HttpResponse('')


@csrf_exempt
def InsertSensors(request):
    if request.method=='POST':
        data = json.loads(request.body)

        for i in data:
            room = Rooms.objects.get(roomid=i['roomid'])
            sensor = Sensors.objects.create(sensorname  = i['sensorname'], 
            								sensorstate = i['sensorstate'], 
            								roomid      = room)
            sensor.save()

    return HttpResponse('')


@csrf_exempt
def InsertWaterusage(request):
    if request.method=='POST':
        data = json.loads(request.body)

        for i in data:
            #sensor = Sensors.objects.get(sensorid=i['sensorid'])
            waterusage = Waterusage.objects.create(timestamp    = i['timestamp'],
											       sensorid     = i['sensorid'],
											       endtimestamp = i['endtimestamp'],
											       usage        = i['usage'],
											       cost         = i['cost'])
            waterusage.save()

    return HttpResponse('')

@csrf_exempt
def InsertWaterusageNoEndtime(request):
    if request.method=='POST':
        data = json.loads(request.body)

        for i in data:
            #sensor = Sensors.objects.get(sensorid=i['sensorid'])
            waterusage = Waterusage.objects.create(timestamp    = i['timestamp'],
                                                   sensorid     = i['sensorid'],
                                                   usage        = i['usage'],
                                                   cost         = i['cost'])
            waterusage.save()

    return HttpResponse('')


@csrf_exempt
def InsertWeather(request):
    if request.method=='POST':
        data = json.loads(request.body)

        for i in data:
            weather = Weather.objects.create(timestamp             = i['timestamp'],
											 temperature           = i['temperature'],
											 precipitation         = i['precipitation'],
											 chanceofprecipitation = i['chanceofprecipitation'],
											 state                 = i['state'])
            weather.save()

    return HttpResponse('')



# Living Nightmare

@csrf_exempt
def InsertLivewaterusage(request):
    if request.method=='POST':
        data = json.loads(request.body)

        for i in data:
            #sensor = Sensors.objects.get(sensorid=i['sensorid'])
            waterusage = Livewaterusage.objects.create(timestamp    = i['timestamp'],
                                                       sensorid     = i['sensorids'],
                                                       endtimestamp = i['endtimestamp'],
                                                       usage        = i['usage'],
                                                       cost         = i['cost'])
            waterusage.save()

    return HttpResponse('')

@csrf_exempt
def InsertLivewaterusageNoEndtime(request):
    if request.method=='POST':
        data = json.loads(request.body)

        for i in data:
            #sensor = Sensors.objects.get(sensorid=i['sensorid'])
            waterusage = Livewaterusage.objects.create(timestamp    = i['timestamp'],
                                                       sensorid     = i['sensorids'],
                                                       usage        = i['usage'],
                                                       cost         = i['cost'])
            waterusage.save()

    return HttpResponse('')


@csrf_exempt
def InsertLivepowerusage(request):
    if request.method=='POST':
        data = json.loads(request.body)

        for i in data:
            #sensor = Sensors.objects.get(sensorid=i['sensorid'])
            powerusage = Livepowerusage.objects.create(timestamp    = i['timestamp'],
                                                       sensorid     = i['sensorids'],
                                                       endtimestamp = i['endtimestamp'],
                                                       usage        = i['usage'],
                                                       cost         = i['cost'])
            powerusage.save()

    return HttpResponse('')

@csrf_exempt
def InsertLivepowerusageNoEndtime(request):
    if request.method=='POST':
        data = json.loads(request.body)

        for i in data:
            #sensor = Sensors.objects.get(sensorid=i['sensorid'])
            powerusage = Livewaterusage.objects.create(timestamp    = i['timestamp'],
                                                       sensorid     = i['sensorids'],
                                                       usage        = i['usage'],
                                                       cost         = i['cost'])
            powerusage.save()

    return HttpResponse('')


class LivewaterusageAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = LivewaterusageSerializer

    def get_queryset(self):
        qs = Livewaterusage.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(timestamp__icontains=query)|
                           Q(sensorids__icontains=query)|
                           Q(endtimestamp__icontains=query)|
                           Q(usage__icontains=query)|
                           Q(cost__icontains=query)).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(timestamp=self.request.timestamp)


class LivepowerusageAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = LivepowerusageSerializer

    def get_queryset(self):
        qs = Livepowerusage.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(timestamp__icontains=query)|
                           Q(sensorids__icontains=query)|
                           Q(endtimestamp__icontains=query)|
                           Q(usage__icontains=query)|
                           Q(cost__icontains=query)).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(timestamp=self.request.timestamp)


