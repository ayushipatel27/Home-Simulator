

from django.urls import path, re_path

from .views import AppliancesAPIView, DailyusageAPIView, EnergyusageAPIView, HvacusageAPIView, RoomsAPIView, SensorsAPIView, WaterusageAPIView, WeatherAPIView, AppliancesRudView, DailyusageRudView, EnergyusageRudView, HvacusageRudView, RoomsRudView, SensorsRudView, WaterusageRudView, WeatherRudView

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

]