

from django.urls import path, re_path

from .views import AppliancesRudView, DailyusageRudView, EnergyusageRudView, HvacusageRudView, RoomsRudView, SensorsRudView, WaterusageRudView, WeatherRudView

urlpatterns = [

	#re_path(r'^(?P<applianceid>\d+)/$', AppliancesRudView.as_view(), name='appliances-rud')

    path('appliances/', AppliancesRudView.as_view(), name='appliances-rud'),

    path('appliances', AppliancesRudView.as_view(), name='appliances-rud'),

    path('dailyusage', DailyusageRudView.as_view(), name='dailyusage-rud'),

    path('energyusage', EnergyusageRudView.as_view(), name='energyusage-rud'),

    path('hvacusage', HvacusageRudView.as_view(), name='hvacusage-rud'),

    path('rooms', RoomsRudView.as_view(), name='rooms-rud'),

    path('sensors', SensorsRudView.as_view(), name='sensors-rud'),

    path('waterusage', WaterusageRudView.as_view(), name='waterusage-rud'),

    path('weather', WeatherRudView.as_view(), name='weather-rud'),

]