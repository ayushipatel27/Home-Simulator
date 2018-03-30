

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

                     GetSensors,
                     GetSensorsTurnedOn,
                     GetAppliances,
                     GetWeekOfPower,
                     GetWeekOfWater,
                     GetMonthOfPower,
                     GetMonthOfWater,

                     InsertSensors, 
                     InsertAppliances, 
                     InsertRooms, 
                     InsertDailyusage, 
                     InsertPowerusage, 
                     InsertHvacusage, 
                     InsertWaterusage, 
                     InsertWeather,

                     InsertLivewaterusage,
                     InsertLivepowerusage,

                     InsertPowerusageNoEndtime, 
                     InsertHvacusageNoEndtime,
                     InsertWaterusageNoEndtime,

                     InsertLivewaterusageNoEndtime,
                     InsertLivepowerusageNoEndtime,

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

    # Individual Views:

    path('appliances/<int:applianceid>/', AppliancesRudView.as_view(), name='appliances-rud'),

    path('dailyusage/<int:dailyusageid>/', DailyusageRudView.as_view(), name='dailyusage-rud'),

    path('powerusage/<int:energyusageid>/', PowerusageRudView.as_view(), name='powerusage-rud'),

    path('hvacusage/<int:hvacusageid>/', HvacusageRudView.as_view(), name='hvacusage-rud'),

    path('rooms/<int:roomid>/', RoomsRudView.as_view(), name='rooms-rud'),

    path('sensors/<int:sensorid>/', SensorsRudView.as_view(), name='sensors-rud'),

    path('waterusage/<int:waterusageid>/', WaterusageRudView.as_view(), name='waterusage-rud'),

    path('weather/<int:weatherid>/', WeatherRudView.as_view(), name='weather-rud'),

    # Get Filtered Lists

    path('getsensors/<int:roomid>/', GetSensors.as_view(), name='get-sensors'), 

    path('inprogress/', GetSensorsTurnedOn.as_view(), name='get-sensors-turned-on'), 

    path('getappliances/<int:sensorid>/', GetAppliances.as_view(), name='get-appliances'),

    path('getweekofusage/', GetWeekOfPower, name='GetWeekOfPower'),

    path('getweekofwater/', GetWeekOfWater, name='GetWeekOfWater'),

    path('getmonthofusage/', GetMonthOfPower, name='GetMonthOfPower'),

    path('getmonthofwater/', GetMonthOfWater, name='GetMonthOfWater'),

    # Inserts

    path('insert/appliances/', InsertAppliances, name='insert-appliances'),

    path('insert/rooms/', InsertRooms, name='insert-rooms'),

    path('insert/sensors/', InsertSensors, name='insert-sensors'),

    path('insert/dailyusage/', InsertDailyusage, name='insert-dailyusage'),

    path('insert/powerusage/', InsertPowerusage, name='insert-powerusage'),

    path('insert/hvacusage/', InsertHvacusage, name='insert-hvacusage'),

    path('insert/waterusage/', InsertWaterusage, name='insert-waterusage'),

    path('insert/weather/', InsertWeather, name='insert-weather'),

    # Inserts without endtimes

    path('insert/powerusagenoendtime/', InsertPowerusageNoEndtime, name='insert-powerusage-no-endtime'),

    path('insert/hvacusagenoendtime/', InsertHvacusageNoEndtime, name='insert-hvacusage-no-endtime'),

    path('insert/waterusagenoendtime/', InsertWaterusageNoEndtime, name='insert-waterusage-no-endtime'),

    # HouseState

    path('gethousestate/', GetCurrentHouseState, name='get-housestate'),

    path('update/housestate/', UpdateHouseState, name='update-housestate'),

    # Living Nightmare

    path('insert/livewaterusage/', InsertLivewaterusage, name='insert-livewaterusage'), 

    path('insert/livepowerusage/', InsertLivepowerusage, name='insert-livepowerusage'),   

    path('insert/livepowerusagenoendtime/', InsertLivepowerusageNoEndtime, name='insert-powerusage-no-endtime'),

    path('insert/livewaterusagenoendtime/', InsertLivewaterusageNoEndtime, name='insert-waterusage-no-endtime'),
]