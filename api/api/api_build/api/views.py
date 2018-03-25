# Generic

from django.db.models import Q
from rest_framework import generics, mixins, viewsets
from django.shortcuts import get_list_or_404, get_object_or_404
#from .models import Post
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse

import json

from rest_framework.generics import UpdateAPIView

from api_build.models import Appliances, Dailyusage, Powerusage, Hvacusage, Rooms, Sensors, Waterusage, Weather
from .serializers import AppliancesSerializer, DailyusageSerializer, PowerusageSerializer, HvacusageSerializer, RoomsSerializer, SensorsSerializer, WaterusageSerializer, WeatherSerializer



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



# class EnergyusageRudView(generics.RetrieveUpdateDestroyAPIView):
# 	lookup_field     = 'energyusageid'
# 	serializer_class = EnergyusageSerializer

# 	def get_queryset(self):
# 		return Energyusage.objects.all()

# 	def put(self, request, *args, **kwargs):
# 		return self.update(request, *args, **kwargs)

# 	def patch(self, request, *args, **kwargs):
# 		return self.update(request, *args, **kwargs)



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
#                       LIST CREATE VIEWS                             #
#######################################################################

class AppliancesViewSet(viewsets.ModelViewSet):
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


def api_update(request):
	instance = get_object_or_404(Rooms)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpRequestRedirect("http://127.0.0.1:8000/api/rooms/1/")

		context = {
			"roomid":1,
			"roomname":"Parent Bedroom"
		}


class UpdateRoom(generics.UpdateAPIView):
    serializer_class = RoomsSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.roomname = request.data.get("roomname")
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

@csrf_exempt
def UpdateRoomNew(request):
    if request.method=='POST':
        data = json.loads(request.body)

        #data2 = json.dumps(data)

        print("\n" + data["roomid"] + "\n")

    return HttpResponseRedirect("/")


#######################################################################
#                       UPDATE STATES                                 #
#######################################################################

@csrf_exempt
def UpdateHouseState(request):
    if request.method=='POST':
        data = json.loads(request.body)

        GetCurrentHouseState()

        #print("\n" + str(data) + "\n")

        # for i in data:
        #     tmp = Rooms.objects.get(roomid=i['roomid'])
        #     tmp.roomname = i['roomname']
        #     tmp.save()

    return HttpResponseRedirect("http://127.0.0.1:8000/api/rooms/")


def GetCurrentHouseState():

    room = Rooms.objects.latest('roomid')

    print("\n" + str(obj.roomname) + "\n")

    return HttpResponseRedirect("http://127.0.0.1:8000/api/rooms/")


#######################################################################
#                       INSERT STATES                                 #
#######################################################################

@csrf_exempt
def InsertAppliances(request):
    if request.method=='POST':
        data = json.loads(request.body)

        for i in data:
            sensor = Sensors.objects.get(sensorid=i['sensorid'])
            appliance = Appliances.objects.create(sensorid=sensor, powerusage=i['powerusage'], powerrate=i['powerrate'], appliancename=i['applianceName'])
            appliance.save()

    return HttpResponse('')

# @csrf_exempt
# def InsertDailyusage(request):
#     if request.method=='POST':
#         data = json.loads(request.body)

#         for i in data:
#             room = Rooms.objects.get(roomid=i['roomid'])
#             tmp = Sensors.objects.create(sensorid=i['sensorid'], sensorname=i['sensorname'], sensorstate=i['sensorstate'], roomid=room)
#             tmp.save()

#     return HttpResponse('')

# @csrf_exempt
# def InsertEnergyusage(request):
#     if request.method=='POST':
#         data = json.loads(request.body)

#         for i in data:
#             room = Rooms.objects.get(roomid=i['roomid'])
#             tmp = Sensors.objects.create(sensorid=i['sensorid'], sensorname=i['sensorname'], sensorstate=i['sensorstate'], roomid=room)
#             tmp.save()

#     return HttpResponse('')


# @csrf_exempt
# def InsertHvacusage(request):
#     if request.method=='POST':
#         data = json.loads(request.body)

#         for i in data:
#             room = Rooms.objects.get(roomid=i['roomid'])
#             tmp = Sensors.objects.create(sensorid=i['sensorid'], sensorname=i['sensorname'], sensorstate=i['sensorstate'], roomid=room)
#             tmp.save()

#     return HttpResponse('')


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
            sensor = Sensors.objects.create(sensorname=i['sensorname'], sensorstate=i['sensorstate'], roomid=room)
            sensor.save()

    return HttpResponse('')


# @csrf_exempt
# def InsertWaterusage(request):
#     if request.method=='POST':
#         data = json.loads(request.body)

#         for i in data:
#             room = Rooms.objects.get(roomid=i['roomid'])
#             tmp = Sensors.objects.create(sensorid=i['sensorid'], sensorname=i['sensorname'], sensorstate=i['sensorstate'], roomid=room)
#             tmp.save()

#     return HttpResponse('')



# @csrf_exempt
# def InsertWeather(request):
#     if request.method=='POST':
#         data = json.loads(request.body)

#         for i in data:
#             room = Rooms.objects.get(roomid=i['roomid'])
#             tmp = Sensors.objects.create(sensorid=i['sensorid'], sensorname=i['sensorname'], sensorstate=i['sensorstate'], roomid=room)
#             tmp.save()

#     return HttpResponse('')



#, appliancename=i['appliancename']










