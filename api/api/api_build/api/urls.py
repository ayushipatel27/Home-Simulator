

from django.urls import path, re_path

from rest_framework.generics import UpdateAPIView

from .views import ( 
                     AppliancesAPIView, 
                     DailyusageAPIView, 
                     PowerusageAPIView, 
                     HvacusageAPIView, 
                     RoomsAPIView, 
                     SensorsAPIView, 
                     WaterusageAPIView, 
                     WeatherAPIView, 

                     AppliancesRudView, 
                     DailyusageRudView, 
                     PowerusageRudView, 
                     HvacusageRudView, 
                     RoomsRudView, 
                     SensorsRudView, 
                     WaterusageRudView, 
                     WeatherRudView,

                     InsertSensors, 
                     InsertAppliances, 
                     InsertRooms, 
                     InsertDailyusage, 
                     InsertPowerusage, 
                     InsertHvacusage, 
                     InsertWaterusage, 
                     InsertWeather,

                     UpdateHouseState,

                     GetCurrentHouseState, 
                    )

urlpatterns = [

	# List Views:

    path('appliances/', AppliancesAPIView.as_view(), name='appliances-listcreate'),

    path('dailyusage/', DailyusageAPIView.as_view(), name='dailyusage-create'),

    path('powerusage/', PowerusageAPIView.as_view(), name='powerusage-listcreate'),

    path('hvacusage/', HvacusageAPIView.as_view(), name='hvacusage-listcreate'),

    path('rooms/', RoomsAPIView.as_view(), name='rooms-listcreate'),

    path('sensors/', SensorsAPIView.as_view(), name='sensors-listcreate'),

    path('waterusage/', WaterusageAPIView.as_view(), name='waterusage-listcreate'),

    path('weather/', WeatherAPIView.as_view(), name='weather-listcreate'),

    path('chs/', GetCurrentHouseState, name='list-chs'),

    # Individual Views:

    path('appliances/<int:applianceid>/', AppliancesRudView.as_view(), name='appliances-rud'),

    path('dailyusage/<int:dailyusageid>/', DailyusageRudView.as_view(), name='dailyusage-rud'),

    path('powerusage/<int:energyusageid>/', PowerusageRudView.as_view(), name='powerusage-rud'),

    path('hvacusage/<int:hvacusageid>/', HvacusageRudView.as_view(), name='hvacusage-rud'),

    path('rooms/<int:roomid>/', RoomsRudView.as_view(), name='rooms-rud'),

    path('sensors/<int:sensorid>/', SensorsRudView.as_view(), name='sensors-rud'),

    path('waterusage/<int:waterusageid>/', WaterusageRudView.as_view(), name='waterusage-rud'),

    path('weather/<int:weatherid>/', WeatherRudView.as_view(), name='weather-rud'),

    # Inserts

    path('insert/appliances/', InsertAppliances, name='insert-appliances'),

    path('insert/rooms/', InsertRooms, name='insert-rooms'),

    path('insert/sensors/', InsertSensors, name='insert-sensers'),

    path('insert/dailyusage/', InsertDailyusage, name='insert-dailyusage'),

    path('insert/powerusage/', InsertPowerusage, name='insert-powerusage'),

    path('insert/hvacusage/', InsertHvacusage, name='insert-hvacusage'),

    path('insert/waterusage/', InsertWaterusage, name='insert-waterusage'),

    path('insert/weather/', InsertWeather, name='insert-weather'),

    # Updates

    path('update/housestate/', UpdateHouseState, name='update-housestate'),
]