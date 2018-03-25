

from django.urls import path, re_path

from rest_framework.generics import UpdateAPIView

from .views import AppliancesAPIView, DailyusageAPIView, EnergyusageAPIView, HvacusageAPIView, RoomsAPIView, SensorsAPIView, WaterusageAPIView, WeatherAPIView, AppliancesRudView, DailyusageRudView, EnergyusageRudView, HvacusageRudView, RoomsRudView, SensorsRudView, WaterusageRudView, WeatherRudView, AppliancesViewSet, api_update, UpdateRoom, UpdateRoomNew, UpdateHouseState, InsertSensors, InsertAppliances, InsertRooms

urlpatterns = [

	# List Create Views:

    path('appliances/', AppliancesAPIView.as_view(), name='appliances-listcreate'),

    path('dailyusage/', DailyusageAPIView.as_view(), name='dailyusage-create'),

    path('energyusage/', EnergyusageAPIView.as_view(), name='energyusage-listcreate'),

    path('hvacusage/', HvacusageAPIView.as_view(), name='hvacusage-listcreate'),

    path('rooms/', RoomsAPIView.as_view(), name='rooms-listcreate'),

    path('sensors/', SensorsAPIView.as_view(), name='sensors-listcreate'),

    path('waterusage/', WaterusageAPIView.as_view(), name='waterusage-listcreate'),

    path('weather/', WeatherAPIView.as_view(), name='weather-listcreate'),

    # Rud Views:

    path('appliances/<int:applianceid>/', AppliancesRudView.as_view(), name='appliances-rud'),

    path('dailyusage/<int:dailyusageid>/', DailyusageRudView.as_view(), name='dailyusage-rud'),

    path('energyusage/<int:energyusageid>/', EnergyusageRudView.as_view(), name='energyusage-rud'),

    path('hvacusage/<int:hvacusageid>/', HvacusageRudView.as_view(), name='hvacusage-rud'),

    path('rooms/<int:roomid>/', RoomsRudView.as_view(), name='rooms-rud'),

    path('sensors/<int:sensorid>/', SensorsRudView.as_view(), name='sensors-rud'),

    path('waterusage/<int:waterusageid>/', WaterusageRudView.as_view(), name='waterusage-rud'),

    path('weather/<int:weatherid>/', WeatherRudView.as_view(), name='weather-rud'),

    # ViewSets:

    path('appliances/viewsets/', AppliancesViewSet.as_view({'get': 'list'}), name='appliances-viewset'),

    # Updates

    path('rooms/aa/', api_update),

    path('updateroom/', UpdateRoom),

    path('updateroomnew/', UpdateRoomNew, name='update-room'),

    path('update/', UpdateHouseState, name='update'),

    # Inserts

    path('insert/appliances/', InsertAppliances, name='insert-appliances'),

    path('insert/rooms/', InsertRooms, name='insert-rooms'),

    path('insert/sensors/', InsertSensors, name='insert-sensers'),
]